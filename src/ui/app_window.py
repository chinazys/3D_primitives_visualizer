from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget)
from PyQt5.QtCore import Qt

from ui.configurator.configurator import Configurator 
from ui.configurator.configurator_types import *
from ui.canvas.canvas import Canvas
from ui.settings import AXIS_MAX_SIZE

APP_WINDOW_ABSOLUTE_WIDTH = 1920
APP_WINDOW_ABSOLUTE_HEIGHT = 1080

class AppWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.window_width, self.window_height = APP_WINDOW_ABSOLUTE_WIDTH, APP_WINDOW_ABSOLUTE_HEIGHT
        
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 32px;
            }
        ''')        

        self.figure = Figure(figsize=(20, 20))
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        self.horizontal_layout = QHBoxLayout(self.central_widget)

        self.all_primitives = []

        self.canvas_layout = Canvas(self)

        self.configurator_layout = Configurator(self)

        self.ax = self.canvas_layout.canvas.figure.add_subplot(projection="3d")
        self.ax.set_xlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_ylim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_zlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)

        self.ax.view_init(30, 30)

        # PICKER ELEMENTS

        # defining default colors first
        self.default_colors = ['#FF0000', '#3F9B0B', '#0000FF', '#00008B', '#461B7E',
                        '#F6BE00', '#C71585', '#FFA500', '#667C26', '#797979']
        # defining dictionary of corresponding picked_on-colors
        self.pick_colors = {'#FF0000': '#FF0000', '#3F9B0B': '#32CD32', '#0000FF': '#1F45FC',
                    '#00008B': '#0000A5', '#461B7E': '#663399', '#F6BE00': '#FDBD01',
                    '#C71585': '#CC338B', '#FFA500': '#FFA62F', '#667C26': '#808000',
                    '#797979': '#848482'}
        # create multipick state variable
        self.muiltipick = False

        # connecting the events with its handlers
        self.figure.canvas.mpl_connect('pick_event', self.on_pick)
        self.figure.canvas.mpl_connect('key_press_event', self.press_key)
        self.figure.canvas.mpl_connect('key_release_event', self.release_key)

    def on_pick(self, event):
        artist = event.artist
        color = str(artist.get_label()).split(' ')[1]

        # Меняем цвет выбранной плоскости
        artist.set_facecolor(self.pick_colors[color])
        artist.set_edgecolor(None)
        artist.set_alpha(.8)

        # print("multipick:", self.muiltipick)
        if self.muiltipick == False:
            # print("kids:", len(self.ax.get_children()))
            primitives = self.ax.get_children()
            prims = [p for p in primitives if str(p.get_label()).split(' ')[0] == "plot"]
            for p in prims:
                if p != artist:
                    p.set_facecolor(str(p.get_label()).split()[1])
                    p.set_edgecolor(None)
                    p.set_alpha(.4)

        # Обновляем фигуру
        self.figure.canvas.draw()

    def press_key(self, event):
        print("pressed key")
        if event.key == 'shift':
            self.muiltipick = True
        if event.key == 'u':
            primitives = self.ax.get_children()
            prims = [p for p in primitives if str(p.get_label()).split(' ')[0] == "plot"]
            for p in prims:
                p.set_facecolor(str(p.get_label()).split()[1])
                p.set_edgecolor(None)
                p.set_alpha(.4)
            self.figure.canvas.draw()

    def release_key(self, event):
        print("released key")
        if event.key == 'shift':
            self.muiltipick = False

    def on_primitive_added(self, primitive):
        primitive.build()
        primitive.plot(self.ax, self.canvas_layout.canvas, self.figure, self.default_colors[len(self.all_primitives)])
        
        self.all_primitives.append(primitive)

        print(type(primitive))
        if str(type(primitive)) == "<class 'primitives.plane.plane.Plane'>":
            others = [p for p in self.all_primitives if str(type(p)) != "<class 'primitives.plane.plane.Plane'>"]
            for p in others:
                self.plot_intersection(primitive, p)

    def on_primitive_removed(self, index):
        print('Remove primitive #', index)
        for plot in self.all_primitives[index].plots:
            try:
                plot.remove()
            except:
                try:
                    plot.pop(0).remove()
                except:
                    pass
                
        print(len(self.all_primitives))
        del(self.all_primitives[index])
        print(len(self.all_primitives))
        self.figure.canvas.draw()
        
    def plot_intersection(self, plane, prim):
        # flatten plane coordinates
        x1f = plane.X_saved.flatten()
        y1f = plane.Y_saved.flatten()
        z1f = plane.Z_saved.flatten()

        # flatten the second primitive coordinates
        x2f = np.array(prim.X_saved).flatten()
        y2f = np.array(prim.Y_saved).flatten()
        z2f = np.array(prim.Z_saved).flatten()

        # concatenating coordinates
        c1 = np.stack((x1f, y1f, z1f), axis=-1)
        c2 = np.stack((x2f, y2f, z2f), axis=-1)
        print("c1.shape:", c1.shape)
        print("c2.shape:", c2.shape)

        intersection = np.array([1, 1, 1])

        if c1.shape[0] < c2.shape[1]:
            l = c1.shape[0]
            for i in range(l):
                tmp = np.broadcast_to(c1[i], c2.shape)
                res = np.linalg.norm(c2-tmp, axis=1)
                mask = res < .6  # create a boolean mask
                result = c2[mask]
                if len(result) > 0:
                    intersection = np.vstack((intersection, result))
        else:
            l = c2.shape[0]
            for i in range(l):
                tmp = np.broadcast_to(c2[i], c1.shape)
                res = np.linalg.norm(c1-tmp, axis=1)
                mask = res < .6  # create a boolean mask
                result = tmp[mask]
                if len(result) > 0:
                    intersection = np.vstack((intersection, result))
        intersection = np.vstack((intersection, intersection[1]))

        # creating array of faces for intersection polygon

        fs = []
        for i in range(intersection.shape[0]-1):
            fs.append([1, i, i+1])
        faces = np.array(fs)

        print("shape:", intersection.shape)
        if intersection.shape[1] > 2:
            self.ax.plot(intersection[1:, 0], intersection[1:, 1], intersection[1:, 2], color='#8C47C6', linewidth=5)
            poly3d = Poly3DCollection(intersection[faces], facecolor='#8C47C6', edgecolors=None, alpha=.8)
            self.ax.add_collection3d(poly3d)
