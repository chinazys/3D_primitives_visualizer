from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.point.point import Point
import numpy as np
from matplotlib.animation import FuncAnimation

# class defining fixed move of a line
# 2 input params: curve 'base' and fixation dot 'fixdot'
class ConicalSurface(Primitive):
    """A class representing a conical surface formed by connecting a base curve to a fixation dot.

    - Attributes:
        - base (Curve): The base curve of the conical surface.
        - fixdot (Point): The fixation dot of the conical surface.
        - _x (list): Temporary storage for x-coordinates of surface fragments.
        - _y (list): Temporary storage for y-coordinates of surface fragments.
        - _z (list): Temporary storage for z-coordinates of surface fragments.
        - tmp_x (list): Temporary storage for x-coordinates of surface fragments (used during animation).
        - tmp_y (list): Temporary storage for y-coordinates of surface fragments (used during animation).
        - tmp_z (list): Temporary storage for z-coordinates of surface fragments (used during animation).
        - surfaces (list): List of plotted surface fragments.
        - surf: The final plotted surface.
        - X_saved (list): Temporary storage for x-coordinates of surface fragments (used during animation).
        - Y_saved (list): Temporary storage for y-coordinates of surface fragments (used during animation).
        - Z_saved (list): Temporary storage for z-coordinates of surface fragments (used during animation).
        - ALPHA (float): The opacity level of the surface (0.0 to 1.0).
        - DOTS (int): The number of dots on the base curve.
        - LENGTH (int): The number of dots taken from the curve to build the animated conical surface.
        - STEP (int): The step size for selecting dots from the base curve.
        - TMP_RESOLUTION (int): The number of dots in each line from the curve to the fixdot.
        - PAUSE (float): The pause time in seconds between fixdot, base curve, and surface plots.
        - INTERVAL (int): The interval between frames in the animation.
        - BIAS (int): The bias value to adjust for initial frames in the animation.
        - plots (list): List of plotted objects.

    - Methods:
        - build(): This method builds the conical surface but is not implemented in this version.
        - plot(ax, canvas, fig): Plots the conical surface on the given axes, canvas, and figure.

    """
    def __init__(self, base: Curve, fixdot: Point):
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
        self.INTERVAL = 750
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 4
        self.plots = []

    def build(self):
        pass
    
    # Updated plot() function with implemented animation
    def plot(self, ax, canvas, fig):
        # defined function for creating i-th frame of animation
        def animate(i):
            # firstly, plot the fixdot
            if i == 0:                    
                self.plots.append(ax.scatter(self.fixdot.x, self.fixdot.y, self.fixdot.z, color='red', s=40))
                if self.flag_text == True:
                    crds = [self.fixdot.x, self.fixdot.y, self.fixdot.z+5]
                    self.plots.append(ax.text(*crds, f"{self.fixdot.primitive_name}", fontsize=15))
                canvas.draw()
                return
            # next, plot the base curve                
            elif i == 1:
                self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5))
                if self.flag_text == True:
                    crds = [self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]-15]
                    self.plots.append(ax.text(*crds, f"{self.base.primitive_name}", fontsize=15))
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
                x0, y0, z0 = self.fixdot.x, self.fixdot.y, self.fixdot.z
                x1, y1, z1 = self.base.x_list[0], self.base.y_list[0], self.base.z_list[0]
                self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color=self.primitive_color, linewidth=5))
                canvas.draw()
                self.INTERVAL = 100
                return
            # if it's the last dot, unite all the fragments into single surface
            if (i-self.BIAS)*(self.STEP) >= self.DOTS-1:
                x0, y0, z0 = self.fixdot.x, self.fixdot.y, self.fixdot.z
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
                surf = ax.plot_surface(X, Y, Z, color=self.primitive_color, alpha=self.primitive_opacity, picker=False)
                # self.plots.append(surf)
                self.surfaces.append(surf)
                self._x.clear()
                self._y.clear()
                self._z.clear()     
                self.X = np.array(self.tmp_x)
                self.Y = np.array(self.tmp_y)
                self.Z = np.array(self.tmp_z)
                for s in self.surfaces:
                    s.remove()
                lbl = "plot " + self.primitive_color
                self.surf = ax.plot_surface(self.X, self.Y, self.Z, label=lbl, alpha=self.primitive_opacity, color=self.primitive_color, picker=True, zorder=1)
                if self.flag_text == True:
                    crds = [(self.fixdot.x+self.base.x_list[0])/2+5, (self.fixdot.y+self.base.y_list[0])/2+5, (self.fixdot.z+self.base.z_list[0])/2+5]
                    self.plots.append(ax.text(*crds, f"{self.primitive_name}", fontsize=15))
                self.plots.append(self.surf)
                canvas.draw()
                return True                
            # usually, we just add another set of dots to the list
            else:
                i -= self.BIAS
                x0, y0, z0 = self.fixdot.x, self.fixdot.y, self.fixdot.z
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
                surf = ax.plot_surface(X, Y, Z, color=self.primitive_color, alpha=self.primitive_opacity)
                self.surfaces.append(surf)
                self.plots.append(surf)
                # self.plots.append(self.surf)
                tmp = [self._x[1], self._y[1], self._z[1]]
                self._x.clear()
                self._y.clear()
                self._z.clear()
                self._x.append(tmp[0])
                self._y.append(tmp[1])
                self._z.append(tmp[2])
                canvas.draw()
        
        if self.flag_animation == True:
            anim = FuncAnimation(fig, animate, frames=self.LENGTH+1+self.BIAS, repeat=False, interval=self.INTERVAL, cache_frame_data=False, save_count=0)
        else:
            for i in range(self.LENGTH+1+self.BIAS):
                animate(i)
        canvas.draw()
