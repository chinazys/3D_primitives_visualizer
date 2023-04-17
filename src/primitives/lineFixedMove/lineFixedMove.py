from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np


def boundCoordinates(fixdot, dot):
    x0, y0, z0 = fixdot
    #print(xyz)
    x1, y1, z1 = dot
    #v = [xyz[0] - x1, xyz[1] - y1, xyz[2] - z1]
    v = [x0 - x1, y0 - y1, z0 - z1]
    k = 0.1

    return [[x0+v[0]*k, x1-v[0]*k], [y0+v[1]*k, y1-v[1]*k], [z0+v[2]*k, z1-v[2]*k]]

# conical surface class
# 2 input params: curve 'base' and fixation dot 'fixdot'
class lineFixedMove(Primitive):
    def __init__(self, base: Curve, fixdot: list):
        self.base = base
        self.fixdot = fixdot
        #print(self.fixdot)

    def build(self):
        pass

    def plot(self, ax, canvas):
        try:
            self.base.build()
            ax.scatter(self.fixdot[0], self.fixdot[1], self.fixdot[2], color='red', s=10)

            ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5)

            _x = []
            _y = []
            _z = []

            for i in range(len(self.base.x_list)):
                xs, ys, zs = boundCoordinates(self.fixdot, (self.base.x_list[i], self.base.y_list[i], self.base.z_list[i]))
                xx = np.linspace(xs[0], xs[1], 5)
                yy = np.linspace(ys[0], ys[1], 5)
                zz = np.linspace(zs[0], zs[1], 5)
                _x.append(xx)
                _y.append(yy)
                _z.append(zz)
            x = np.array(_x)
            y = np.array(_y)
            z = np.array(_z)
            ax.plot_surface(x, y, z, alpha=.85, color='#579def')
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')
