from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation

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
        self.X = None
        self.Y = None
        self.Z = None
        self.X_saved = []
        self.Y_saved = []
        self.Z_saved = []
        
        # GENERAL PARAMETERS: are applied when plotting both animated and result surfaces
        self.ALPHA = .4  # sets capacity level
        self.DOTS = len(self.base.x_list)  # sets the number of curve dots

        # ANIMATION PARAMETERS: are apllied when plotting animated surface
        self.LENGTH = 20  # sets the number of dots we take from the curve to build the conical surface
        self.STEP = self.DOTS//self.LENGTH  # calculates the step of taking next dot to expand the animated conical surface
        self.TMP_RESOLUTION = 2  # number of dots each line from curve to fixdot contains
        self.PAUSE = 1  # sets pause time in seconds between fixdot, base curve and the surface plots
        self.INTERVAL = 100
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 4

    def build(self):
        pass
    
    # Updated plot() function with implemented animation
    def plot(self, ax, canvas, fig, _color):
        try:            
            # defined function for creating i-th frame of animation
            def animate(i):
                # firstly, plot the fixdot
                if i == 0:                    
                    self.plots.append(ax.scatter(*self.fixdot, color='red', s=40))
                    canvas.draw()
                    return
                # next, plot the base curve                
                elif i == 1:
                    self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5))
                    canvas.draw()
                    return
                # then, plot P dot (the first base-curve dot in the list)
                elif i == 2:
                    x1, y1, z1 = self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]
                    self.plots.append(ax.scatter(x1, y1, z1, color='red', s=40))
                    canvas.draw()
                    return
                # finally, plot connecting line between P dot and fixdot
                elif i == 3:
                    x0, y0, z0 = self.fixdot
                    x1, y1, z1 = self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]
                    self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color=_color, linewidth=5))
                    canvas.draw()
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
                    surf = ax.plot_surface(X, Y, Z, color=_color, alpha=self.ALPHA, picker=False)
                    self.plots.append(surf)
                    self.surfaces.append(surf)
                    self._x.clear()
                    self._y.clear()
                    self._z.clear()     
                    self.X = np.array(self.tmp_x)
                    self.Y = np.array(self.tmp_y)
                    self.Z = np.array(self.tmp_z)
                    for s in self.surfaces:
                        s.remove()
                    lbl = "plot " + _color
                    self.surf = ax.plot_surface(self.X, self.Y, self.Z, label=lbl, alpha=self.ALPHA, color=_color, picker=True, zorder=1)
                    canvas.draw()
                    self.plots.append(self.surf)
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
                    
                    
                    # xx = np.linspace(x0, self.base.x_list[i*self.STEP//2], 200)
                    # yy = np.linspace(y0, self.base.y_list[i*self.STEP//2], 200)
                    # zz = np.linspace(z0, self.base.z_list[i*self.STEP//2], 200)
                    # self.X_saved.append(xx)
                    # self.Y_saved.append(yy)
                    # self.Z_saved.append(zz)
                    xx = np.linspace(x0, self.base.x_list[i*self.STEP], 200)
                    yy = np.linspace(y0, self.base.y_list[i*self.STEP], 200)
                    zz = np.linspace(z0, self.base.z_list[i*self.STEP], 200)
                    self.X_saved.append(xx)
                    self.Y_saved.append(yy)
                    self.Z_saved.append(zz)
                # and if there are 2 sets of dots, we plot a surface fragment between them
                if len(self._x) == 2:
                    X = np.array(self._x)
                    Y = np.array(self._y)
                    Z = np.array(self._z)
                    surf = ax.plot_surface(X, Y, Z, color=_color, alpha=self.ALPHA)
                    self.surfaces.append(surf)
                    self.plots.append(self.surf)
                    tmp = [self._x[1], self._y[1], self._z[1]]
                    self._x.clear()
                    self._y.clear()
                    self._z.clear()
                    self._x.append(tmp[0])
                    self._y.append(tmp[1])
                    self._z.append(tmp[2])
                    canvas.draw()
            anim = FuncAnimation(fig, animate, frames=self.LENGTH+1+self.BIAS, repeat=False, interval=self.INTERVAL, cache_frame_data=False, save_count=0)
            canvas.draw()            
        except:
            print('Surface is invalid => cannot plot')
