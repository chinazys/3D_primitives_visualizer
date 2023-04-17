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

# class defining fixed move of a line
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

            for i in range(len(self.base.x_list)):
                xs, ys, zs = boundCoordinates(self.fixdot, (self.base.x_list[i], self.base.y_list[i], self.base.z_list[i]))
                ax.plot(xs, ys, zs, color='#579def', linewidth=3, alpha=.05)
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')
