from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget, QMessageBox)

from ui.configurator.configurator import Configurator 
from ui.configurator.configurator_types import *
from ui.canvas.canvas import Canvas
from ui.settings import AXIS_MAX_SIZE, APP_WINDOW_MIN_WIDTH, APP_WINDOW_MIN_HEIGHT
from util.shift_color import shift_color

class AppWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.window_width, self.window_height = APP_WINDOW_MIN_WIDTH, APP_WINDOW_MIN_HEIGHT
        
        self.setMinimumSize(self.window_width, self.window_height)
        self.showMaximized()
        self.setStyleSheet('''
            QWidget {
                font-size: 32px;
            }
        ''')        
        self.setWindowTitle('3D Primitives Visualizer')
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
        
        # Added axes labels and colors
        self.ax.tick_params(axis='x', colors='red')
        self.ax.tick_params(axis='y', colors='green')
        self.ax.tick_params(axis='z', colors='blue')

        self.ax.set_xlabel('X', fontsize=17, fontweight='demibold', fontfamily='serif')
        self.ax.set_ylabel('Y', fontsize=17, fontweight='demibold', fontfamily='serif')
        self.ax.set_zlabel('Z', fontsize=17, fontweight='demibold', fontfamily='serif')

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

    def show_error(self, title:str="Error", text:str="Unknown"):
        QMessageBox.critical(self, title, text)

    def on_pick(self, event):
        artist = event.artist

        # print("multipick:", self.muiltipick)
        # print("kids:", len(self.ax.get_children()))
        artists = self.ax.get_children()
        prims = [p for p in artists if str(p.get_label()).split(' ')[0] == "plot"]
        
        for i, primitive in enumerate(self.all_primitives):
            if primitive.primitive_type == CONFIGURATOR_TYPE_LINE or primitive.primitive_type == CONFIGURATOR_TYPE_CURVE:
                prims.insert(i, None)
        
        for i, p in enumerate(prims):
            if p is None:
                continue

            p.set_edgecolor(None)
            if p == artist:
                p.set_alpha(min(self.all_primitives[i].primitive_opacity * 1.6, 1))
                p.set_facecolor(shift_color(self.all_primitives[i].primitive_color))
            elif self.muiltipick == False:
                p.set_alpha(self.all_primitives[i].primitive_opacity)
                p.set_facecolor(self.all_primitives[i].primitive_color)

        # Обновляем фигуру
        self.figure.canvas.draw()

    def press_key(self, event):
        if event.key == 'shift' or event.key == 'enter' or event.key == 'p':
            self.muiltipick = True
        if event.key == 'escape' or event.key == ' ' or event.key == 'u':
            primitives = self.ax.get_children()
            prims = [p for p in primitives if str(p.get_label()).split(' ')[0] == "plot"]
            for i, primitive in enumerate(self.all_primitives):
                if primitive.primitive_type == CONFIGURATOR_TYPE_LINE or primitive.primitive_type == CONFIGURATOR_TYPE_CURVE:
                    prims.insert(i, None)

            for i, p in enumerate(prims):
                if p is None:
                    continue
                p.set_edgecolor(None)
                p.set_alpha(self.all_primitives[i].primitive_opacity)
                p.set_facecolor(self.all_primitives[i].primitive_color)
            self.figure.canvas.draw()

    def release_key(self, event):
        if event.key == 'shift' or event.key == 'enter' or event.key == 'p':
            self.muiltipick = False

    def on_primitive_added(self, primitive, index=-1):
        primitive.build()
        primitive.plot(self.ax, self.canvas_layout.canvas, self.figure)
        
        if index == -1:
            self.all_primitives.append(primitive)
        else:
            self.all_primitives.insert(index, primitive)

        planes = [p for p in self.all_primitives if p.primitive_type == CONFIGURATOR_TYPE_PLANE]
        others = [p for p in self.all_primitives if p.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE or p.primitive_type == CONFIGURATOR_TYPE_LINEMOVE or p.primitive_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE]

        if primitive in planes:
            for other in others:
                try:
                    self.plot_intersection(primitive, other)
                except:
                    pass
        elif primitive in others:
            for plane in planes:
                try:
                    self.plot_intersection(plane, primitive)
                except:
                    pass

    def on_primitive_edited(self, primitive, primitive_index):
        self.on_primitive_removed(primitive_index)
        self.on_primitive_added(primitive, index=primitive_index)

    def on_primitive_visibility_changed(self, index, is_visible):
        for plot in self.all_primitives[index].plots:
            try:
                if is_visible:
                    plot.set_alpha(self.all_primitives[index].primitive_opacity)
                else:
                    plot.set_alpha(0.0)
            except:
                for subplot in plot:
                    if is_visible:
                        subplot.set_alpha(self.all_primitives[index].primitive_opacity)
                    else:
                        subplot.set_alpha(0.0)
        
        self.figure.canvas.draw()

    def on_primitive_removed(self, index):
        for plot in self.all_primitives[index].plots:
            try:
                plot.remove()
            except:
                try:
                    plot.pop(0).remove()
                except:
                    pass
                
        del(self.all_primitives[index])
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

        if intersection.shape[1] > 2:
            border_plot = self.ax.plot(intersection[1:, 0], intersection[1:, 1], intersection[1:, 2], color='#8C47C6', linewidth=5)
            poly3d = Poly3DCollection(intersection[faces], facecolor='#8C47C6', edgecolors=None, alpha=.9)
            surface_plot = self.ax.add_collection3d(poly3d)

            plane.plots.append(border_plot)
            plane.plots.append(surface_plot)

            prim.plots.append(border_plot)
            prim.plots.append(surface_plot)
