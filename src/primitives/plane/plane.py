from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.point.point import Point
import numpy as np
from matplotlib.animation import FuncAnimation


class Plane(Primitive):
    def __init__(self, M: Point, n: Point):
        self.M = M
        self.n = n
        # ANIMATION PARAMETERS
        # 3 animation frames for M dot, n vector and the plane itself
        self.FRAMES = 3
        self.INTERVAL = 500
        self.plots = []

    def _fill_points_list(self):
        self.x_list = np.linspace(-100, 100, 2)
        self.y_list = np.linspace(-100, 100, 2)
        self.X_list, self.Y_list = np.meshgrid(self.x_list, self.y_list)

        m1, m2, m3 = self.M.x, self.M.y, self.M.z
        n1, n2, n3 = self.n.x, self.n.y, self.n.z
        
        self.Z_list = (-n1*self.X_list+n1*m1-n2*self.Y_list+n2*m2+n3*m3) / n3

        self.x_saved = np.linspace(-100, 100, 200)
        self.y_saved = np.linspace(-100, 100, 200)
        self.X_saved, self.Y_saved = np.meshgrid(self.x_saved, self.y_saved)
        self.Z_saved = (-n1*self.X_saved+n1*m1-n2*self.Y_saved+n2*m2+n3*m3) / n3


    def build(self):
        self._fill_points_list()
        pass

    def plot(self, ax, canvas, fig):
        try:
            def animate(i):
                if i == 0:
                    self.plots.append(ax.scatter(self.M.x, self.M.y, self.M.z, s=15, color='red'))
                    if self.flag_text == True:
                        label = "{}: ({}; {}; {})".format(self.M.primitive_name, self.M.x, self.M.y, self.M.z)
                        self.plots.append(ax.text(self.M.x+3, self.M.y+3, self.M.z+3, label, fontsize=15))
                    canvas.draw()
                elif i == 1:
                    self.plots.append(ax.quiver(self.M.x, self.M.y, self.M.z, self.n.x, self.n.y, self.n.z, color='g'))
                    if self.flag_text == True:
                        label = "{}: ({}; {}; {})".format(self.n.primitive_name, self.n.x, self.n.y, self.n.z)
                        self.plots.append(ax.text(self.M.x+self.n.x+3, self.M.y+self.n.y+3, self.M.z+self.n.z+3, label, fontsize=15))
                    canvas.draw()
                elif i == 2:
                    lbl = "plot " + self.primitive_color
                    self.plots.append(ax.plot_surface(self.X_list, self.Y_list, self.Z_list, label=lbl, color=self.primitive_color, alpha=self.primitive_opacity, picker=True, zorder=0))
                    if self.flag_text == True:
                        label = "Plane {}".format(self.primitive_name)
                        self.plots.append(ax.text(self.M.x+20, self.M.y+20, self.M.z+20, label, fontsize=15))
                    canvas.draw()

            if self.flag_animation == True:
                plane_anim = FuncAnimation(fig, animate, frames=self.FRAMES, repeat=False, interval=self.INTERVAL)
            else:
                for i in range(3):
                    animate(i)
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')