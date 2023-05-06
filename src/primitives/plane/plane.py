from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation


class Plane(Primitive):
    def __init__(self, M: tuple, n: tuple):
        self.M = M
        self.n = n
        # ANIMATION PARAMETERS
        # 3 animation frames for M dot, n vector and the plane itself
        self.FRAMES = 3
        self.INTERVAL = 500

    def _fill_points_list(self):
        self.x_list = np.linspace(-100, 100, 2)
        self.y_list = np.linspace(-100, 100, 2)
        self.X_list, self.Y_list = np.meshgrid(self.x_list, self.y_list)

        m1, m2, m3 = self.M
        n1, n2, n3 = self.n
        
        self.Z_list = (-n1*self.X_list+n1*m1-n2*self.Y_list+n2*m2+n3*m3) / n3

        self.x_saved = np.linspace(-100, 100, 200)
        self.y_saved = np.linspace(-100, 100, 200)
        self.X_saved, self.Y_saved = np.meshgrid(self.x_saved, self.y_saved)
        self.Z_saved = (-n1*self.X_saved+n1*m1-n2*self.Y_saved+n2*m2+n3*m3) / n3


    def build(self):
        self._fill_points_list()
        pass

    def plot(self, ax, canvas, fig, _color):
        try:
            def animate(i):
                if i == 0:
                    label = "M: ({}; {}; {})".format(self.M[0], self.M[1], self.M[2])
                    ax.scatter(self.M[0], self.M[1], self.M[2], s=15, color='red')
                    ax.text(self.M[0]+3, self.M[1]+3, self.M[2]+3, label, fontsize=15)
                    canvas.draw()
                elif i == 1:
                    label = "n: ({}; {}; {})".format(self.n[0], self.n[1], self.n[2])
                    ax.quiver(self.M[0], self.M[1], self.M[2], self.n[0], self.n[1], self.n[2], color='g')
                    ax.text(self.M[0]+self.n[0]+3, self.M[1]+self.n[1]+3, self.M[2]+self.n[2]+3, label, fontsize=15)
                    canvas.draw()
                elif i == 2:
                    label = "Plane alpha"
                    lbl = "plot " + _color
                    ax.plot_surface(self.X_list, self.Y_list, self.Z_list, label=lbl, color=_color, alpha=.4, picker=True, zorder=0)
                    ax.text(self.M[0]+20, self.M[1]+20, self.M[2]+20, label, fontsize=15)
                    canvas.draw()

            plane_anim = FuncAnimation(fig, animate, frames=self.FRAMES, repeat=False, interval=self.INTERVAL)
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')
