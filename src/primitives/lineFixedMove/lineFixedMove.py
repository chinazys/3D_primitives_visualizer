from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation
# import matplotlib.pyplot as plt
# from PyQt5.QtCore import QTimer
# from time import sleep
# import time

# temporay, this function is not used anywhere below
# def boundCoordinates(fixdot, dot):
#     x0, y0, z0 = fixdot
#     x1, y1, z1 = dot
#     v = [x0 - x1, y0 - y1, z0 - z1]
#     k = 0.1

#     return [[x0+v[0]*k, x1-v[0]*k], [y0+v[1]*k, y1-v[1]*k], [z0+v[2]*k, z1-v[2]*k]]

# class defining fixed move of a line
# 2 input params: curve 'base' and fixation dot 'fixdot'
class lineFixedMove(Primitive):
    def __init__(self, base: Curve, fixdot: list):
        self.base = base
        self.base.build()
        self.fixdot = fixdot
        self._x = []
        self._y = []
        self._z = []
        self.tmp_x = []
        self.tmp_y = []
        self.tmp_z = []
        self.surfaces = []
        self.surf = None
        
        # GENERAL PARAMETERS: are applied when plotting both animated and result surfaces
        self.ALPHA = .75  # sets capacity level
        self.COLOR = '#579def'  # sets the color of the surface
        self.DOTS = len(self.base.x_list)  # sets the number of curve dots

        # ANIMATION PARAMETERS: are apllied when plotting animated surface
        self.LENGTH = 20  # sets the number of dots we take from the curve to build the conical surface
        self.STEP = self.DOTS//self.LENGTH  # calculates the step of taking next dot to expand the animated conical surface
        self.TMP_RESOLUTION = 2  # number of dots each line from curve to fixdot contains
        self.PAUSE = 1  # sets pause time in seconds between fixdot, base curve and the surface plots
        self.INTERVAL = 50
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 4

    def build(self):
        pass
    
    # Updated plot() function with implemented animation
    def plot(self, ax, canvas, fig):
        try:            
            # defined function for creating i-th frame of animation
            def animate(i):
                # firstly, plot the fixdot
                if i == 0:                    
                    ax.scatter(*self.fixdot, color='red', s=40)
                    return
                # next, plot the base curve                
                elif i == 1:
                    ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5)
                    return
                # then, plot P dot (the first base-curve dot in the list)
                elif i == 2:
                    x1, y1, z1 = self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]
                    ax.scatter(x1, y1, z1, color='red', s=40)
                    return
                # finally, plot connecting line between P dot and fixdot
                elif i == 3:
                    x0, y0, z0 = self.fixdot
                    x1, y1, z1 = self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]
                    ax.plot([x0, x1], [y0, y1], [z0, z1], color='blue', linewidth=5)
                    self.INTERVAL = 100
                    return
                # if it's the last dot, unite all the fragments into single surface
                if (i-self.BIAS)*(self.STEP) >= self.DOTS-1:
                    x0, y0, z0 = self.fixdot
                    xx = np.linspace(x0, self.base.x_list[self.DOTS-1], self.TMP_RESOLUTION)
                    yy = np.linspace(y0, self.base.y_list[self.DOTS-1], self.TMP_RESOLUTION)
                    zz = np.linspace(z0, self.base.z_list[self.DOTS-1], self.TMP_RESOLUTION)
                    self._x.append(xx)
                    self._y.append(yy)
                    self._z.append(zz)
                    self.tmp_x.append(xx)
                    self.tmp_y.append(yy)
                    self.tmp_z.append(zz)
                    X = np.array(self._x)
                    Y = np.array(self._y)
                    Z = np.array(self._z)
                    surf = ax.plot_surface(X, Y, Z, color=self.COLOR, alpha=self.ALPHA, picker=False)
                    self.surfaces.append(surf)
                    self._x.clear()
                    self._y.clear()
                    self._z.clear()     
                    X = np.array(self.tmp_x)
                    Y = np.array(self.tmp_y)
                    Z = np.array(self.tmp_z)
                    for s in self.surfaces:
                        s.remove()
                    self.surf = ax.plot_surface(X, Y, Z, alpha=self.ALPHA, color=self.COLOR, picker=True)
                    return True                
                # usually, we just add another set of dots to the list
                else:
                    i -= self.BIAS
                    x0, y0, z0 = self.fixdot
                    xx = np.linspace(x0, self.base.x_list[i*self.STEP], self.TMP_RESOLUTION)
                    yy = np.linspace(y0, self.base.y_list[i*self.STEP], self.TMP_RESOLUTION)
                    zz = np.linspace(z0, self.base.z_list[i*self.STEP], self.TMP_RESOLUTION)
                    self._x.append(xx)
                    self._y.append(yy)
                    self._z.append(zz)
                    self.tmp_x.append(xx)
                    self.tmp_y.append(yy)
                    self.tmp_z.append(zz)
                # and if there are 2 sets of dots, we plot a surface fragment between them
                if len(self._x) == 2:
                    X = np.array(self._x)
                    Y = np.array(self._y)
                    Z = np.array(self._z)
                    surf = ax.plot_surface(X, Y, Z, color=self.COLOR, alpha=self.ALPHA)
                    self.surfaces.append(surf)
                    tmp = [self._x[1], self._y[1], self._z[1]]
                    self._x.clear()
                    self._y.clear()
                    self._z.clear()
                    self._x.append(tmp[0])
                    self._y.append(tmp[1])
                    self._z.append(tmp[2])                     
            anim = FuncAnimation(fig, animate, frames=self.LENGTH+1+self.BIAS, repeat=False, interval=self.INTERVAL)
            canvas.draw()            
        except:
            print('Surface is invalid => cannot plot')
