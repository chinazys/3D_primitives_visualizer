from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation
import time
class rotate_surface(Primitive):
    def __init__(self, base: Curve, dot: list, vector: list):  # line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)

        if vector == [0, 0, 0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(dot) == 3, "dot is invalid"
        assert len(vector) == 3, "vector is invalid"

        self.base = base
        self.base.build()

        self.dot = dot

        self.vector = vector

        # self.main_line = Line([dot, vector + dot])

        # self.main_line.build()
        self._x=[]
        self._y=[]
        self._z=[]
        self.x_list, self.y_list, self.z_list = [], [], []
        self.build()

        self.DOTS = len(self.x_list)  # sets the number of curve dots

        self.LENGTH = len(self.x_list)  # sets the number of dots we take from the curve to build the conical surface
        self.STEP = self.DOTS//self.LENGTH  # calculates the step of taking next dot to expand the animated conical surface
        self.TMP_RESOLUTION = 2  # number of dots each line from curve to fixdot contains
        self.PAUSE = 1  # sets pause time in seconds between fixdot, base curve and the surface plots
        self.INTERVAL = 100
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 3
        self.plots = []


    def build(self):

        def rotate_point_about_line(point, line_point, line_direction, angle):
            # Convert angle to radians
            theta = np.radians(angle)

            # Convert all inputs to numpy arrays for consistency
            point = np.array(point)
            line_point = np.array(line_point)
            line_direction = np.array(line_direction)

            # Calculate unit direction vector
            u = line_direction / np.linalg.norm(line_direction)

            # Calculate rotation matrix
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            u_x = u[0]
            u_y = u[1]
            u_z = u[2]
            rot_mat = np.array([[cos_theta + u_x ** 2 * (1 - cos_theta), u_x * u_y * (1 - cos_theta) - u_z * sin_theta,
                                 u_x * u_z * (1 - cos_theta) + u_y * sin_theta],
                                [u_y * u_x * (1 - cos_theta) + u_z * sin_theta, cos_theta + u_y ** 2 * (1 - cos_theta),
                                 u_y * u_z * (1 - cos_theta) - u_x * sin_theta],
                                [u_z * u_x * (1 - cos_theta) - u_y * sin_theta,
                                 u_z * u_y * (1 - cos_theta) + u_x * sin_theta,
                                 cos_theta + u_z ** 2 * (1 - cos_theta)]])

            # Apply rotation to point
            rotated_point = np.matmul(rot_mat, (point - line_point)) + line_point

            return rotated_point.tolist()

        a, b, c = self.dot
        m, n, p = self.vector

        # ax=self.main_line.plot(ax)

        x = self.base.x_list
        y = self.base.y_list
        z = self.base.z_list

        x_new, y_new, z_new = [], [], []
        x_, y_, z_ = [], [], []

        for j in range(0, 361,10):
            for i in range(0, len(x)):
                theta = j
                x_rot, y_rot, z_rot = rotate_point_about_line(np.array([x[i], y[i], z[i]]), np.array([a, b, c]),
                                                         np.array([m, n, p]), theta)
                x_new.append(x_rot)
                y_new.append(y_rot)
                z_new.append(z_rot)
            x_.append(x_new)
            y_.append(y_new)
            z_.append(z_new)
            x_new, y_new, z_new = [], [], []



        self.x_list = x_
        self.y_list = y_
        self.z_list = z_

    def plot(self, ax, canvas, fig, _color):
        

        def animate(i):
                #print(len(self.x_list[i-self.BIAS]),len(self.y_list[i-self.BIAS]),len(self.z_list[i-self.BIAS]))
                if i==6:
                    return
                
                # firstly, plot the fixdot
                if i == 0:
                    self.plots.append(ax.scatter(*self.dot, color='red', s=40))
                    canvas.draw()
                    
                    
                                  
                    
                # next, plot the base curve                
                elif i == 1:
                    x0, y0, z0 = [-self.vector[i]*20 +self.dot[i] for i in range(3) ]
                    x1, y1, z1 = [self.vector[i]*20+self.dot[i] for i in range(3) ]
                    self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color=_color, linewidth=5))
                    canvas.draw()
                    
                    
                    
                    
                # finally, plot connecting line between P dot and fixdot
                elif i == 2:
                    self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5))
                    canvas.draw()
                    
                    
                # if it's the last dot, unite all the fragments into single surface
                elif (len(self.x_list)+self.BIAS) ==i:
                    
                    self._x.append(self.x_list[-1])
                    self._y.append(self.y_list[-1])
                    self._z.append(self.z_list[-1])
                    self.plots.append(ax.plot_surface(np.array(self._x),np.array(self._y),np.array(self._z),alpha=0.4,color='b'))
                    canvas.draw()
                    
                    
                else:
                    
                # usually, we just add another set of dots to the list
                    
                    self._x.append(self.x_list[(i-self.BIAS)])
                    self._y.append(self.y_list[(i-self.BIAS)])
                    self._z.append(self.z_list[(i-self.BIAS)])
                    
                    
                    
                    
                    if len(self._x)==2:
                        #print(self._x,self._y,self._z)
                        #print(self._x,'\n')
                        self.plots.append(ax.plot_surface(np.array(self._x),np.array(self._y),np.array(self._z),alpha=0.4,color='b'))
                        self._x.pop(0)
                        
                        self._y.pop(0)
                        self._z.pop(0)
                        canvas.draw()
                
                        
                
        
        anim = FuncAnimation(fig, animate, frames=(len(self.x_list)+self.BIAS), repeat=False, interval=750,cache_frame_data=False, save_count=0)

        canvas.draw()