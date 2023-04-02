import numpy as np
from primitives.primitive import Primitive

class Surface(Primitive):
    def generate_points(self):
        self.X, self.Y = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))
        self.Z = np.sin(np.sqrt(self.X ** 2 + self.Y ** 2))
        return (self.X, self.Y, self.Z)
    def plot(self, ax, canvas):
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap="viridis", edgecolor="none")
        canvas.draw()