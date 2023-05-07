from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation


class Plane(Primitive):
    plots = []

    def __init__(self, M: tuple, n: tuple):
        self.M = M
        self.n = n
        # ANIMATION PARAMETERS
        # 3 animation frames for M dot, n vector and the plane itself
        self.FRAMES = 3
        self.INTERVAL = 1000

    def _fill_points_list(self):
        self.x_list = np.linspace(-100, 100, 50)
        self.y_list = np.linspace(-100, 100, 50)
        self.X_list, self.Y_list = np.meshgrid(self.x_list, self.y_list)

        m1, m2, m3 = self.M
        n1, n2, n3 = self.n
        
        self.Z_list = (-n1*self.X_list+n1*m1-n2*self.Y_list+n2*m2+n3*m3) / n3

    def build(self):
        self._fill_points_list()
        pass

    def plot(self, ax, canvas, fig):
        try:
            def animate(i):
                if i == 0:
                    label = "M: ({}; {}; {})".format(self.M[0], self.M[1], self.M[2])
                    self.plots.append(ax.scatter(self.M[0], self.M[1], self.M[2], s=15, color='red'))
                    self.plots.append(ax.text(self.M[0]+3, self.M[1]+3, self.M[2]+3, label, fontsize=15))
                elif i == 1:
                    label = "n: ({}; {}; {})".format(self.n[0], self.n[1], self.n[2])
                    self.plots.append(ax.quiver(self.M[0], self.M[1], self.M[2], self.n[0], self.n[1], self.n[2], color='g'))
                    self.plots.append(ax.text(self.M[0]+self.n[0]+3, self.M[1]+self.n[1]+3, self.M[2]+self.n[2]+3, label, fontsize=15))
                elif i == 2:
                    label = "Plane alpha"
                    self.plots.append(ax.plot_surface(self.X_list, self.Y_list, self.Z_list, color='#579def', alpha=.6, picker=True))
                    self.plots.append(ax.text(self.M[0]+20, self.M[1]+20, self.M[2]+20, label, fontsize=15))

            anim = FuncAnimation(fig, animate, frames=self.FRAMES, repeat=False, interval=self.INTERVAL)
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')