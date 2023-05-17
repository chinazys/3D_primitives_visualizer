from primitives.curve.curve import Curve
from primitives.primitive import Primitive
import numpy as np
from matplotlib.animation import FuncAnimation
import time
class rotate_surface(Primitive):
    def __init__(self, base: Curve, dot, vector):  # line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)
        self.point_saved = dot
        self.vector_saved = vector
        
        self.dot = [dot.x,dot.y,dot.z]
        self.vector = [vector.x,vector.y,vector.z]
        #print(self.vector)
        if self.vector == [0, 0, 0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(self.dot) == 3, "dot is invalid"
        assert len(self.vector) == 3, "vector is invalid"
        self.surfaces=[]
        self.base = base
        self.base.build()




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
        self.BIAS = 4
        self.plots = []

        self.label_point=dot.primitive_name
        self.label_vector = vector.primitive_name
        self.label_curve=base.primitive_name

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

    def plot(self, ax, canvas, fig):
        def animate(i):
                #print(len(self.x_list[i-self.BIAS]),len(self.y_list[i-self.BIAS]),len(self.z_list[i-self.BIAS]))

                
                # firstly, plot the fixdot
                if i == 0:
                    if self.flag_text:
                        self.plots.append(ax.text(self.dot[0], self.dot[1], self.dot[2] + 1,
                                                  "{}: ({}; {}; {})".format(self.label_point, self.dot[0], self.dot[1],
                                                                            self.dot[2]), fontsize=10))

                    self.plots.append(ax.scatter(*self.dot, color='red', s=40))
                    canvas.draw()
                    
                    
                                  
                elif i==1:
                    x2, y2, z2 = self.dot
                    x3, y3, z3 = [self.vector[i] + self.dot[i] for i in range(3)]
                    if self.flag_text:
                        self.plots.append(ax.text(self.dot[0] + self.vector[0], self.dot[1] + self.vector[1],
                                              self.dot[2] + self.vector[2],
                                              "{}: ({}; {}; {})".format(self.label_vector, self.vector[0],
                                                                        self.vector[1], self.vector[2]),
                                              (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
                    self.plots.append(ax.plot([x2, x3], [y2, y3], [z2, z3], color='green', linewidth=7))
                    canvas.draw()

                # next, plot the base curve                
                elif i == 2:
                    x0, y0, z0 = [-self.vector[i]*20 +self.dot[i] for i in range(3) ]
                    x1, y1, z1 = [self.vector[i]*20+self.dot[i] for i in range(3) ]
                    if self.flag_text:
                        self.plots.append(ax.text(-self.vector[0] * 2 + self.dot[0], -self.vector[1] * 2 + self.dot[1],
                                                  -self.vector[2] * 2 + self.dot[2], self.label_vector,
                                                  (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
                    self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color='blue', linewidth=5))
                    canvas.draw()

                    
                    
                    
                    
                # finally, plot connecting line between P dot and fixdot
                elif i == 3:
                    if self.flag_text:
                        self.plots.append(ax.text(self.base.x_list[0], self.base.y_list[0], self.base.z_list[0],
                                                  self.label_curve,
                                                  (self.base.x_list[1], self.base.y_list[1], self.base.z_list[1]),
                                                  fontsize=10))
                    self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color=self.primitive_color, linewidth=5))
                    canvas.draw()
                    
                    
                # if it's the last dot, unite all the fragments into single surface
                elif len(self.x_list)+self.BIAS == i+1:

                    for s in self.surfaces:
                        s.remove()

                    self.plots.append(ax.plot_surface(np.array(self.x_list), np.array(self.y_list), np.array(self.z_list),label = "plot ", color=self.primitive_color, alpha=self.primitive_opacity,picker=True ))

                    canvas.draw()

                    
                else:
                    
                # usually, we just add another set of dots to the list
                    
                    self._x.append(self.x_list[(i-self.BIAS)])
                    self._y.append(self.y_list[(i-self.BIAS)])
                    self._z.append(self.z_list[(i-self.BIAS)])
                    
                    
                    
                    
                    if len(self._x)==2:
                        #print(self._x,self._y,self._z)
                        #print(self._x,'\n')

                        surf = ax.plot_surface(np.array(self._x), np.array(self._y), np.array(self._z),
                                                    alpha=self.primitive_opacity, color=self.primitive_color
                                                    )
                        self.surfaces.append(surf)
                        self.plots.append(surf)

                        self._x.pop(0)
                        self._y.pop(0)
                        self._z.pop(0)
                        canvas.draw()
                
                        
                
        if self.flag_animation:
            anim = FuncAnimation(fig, animate, frames=(len(self.x_list)+self.BIAS), repeat=False, interval=750,cache_frame_data=False, save_count=0)

            canvas.draw()

        else:

            x0, y0, z0 = [-self.vector[i] * 20 + self.dot[i] for i in range(3)]
            x1, y1, z1 = [self.vector[i] * 20 + self.dot[i] for i in range(3)]
            x2, y2, z2 = self.dot
            x3, y3, z3 = [self.vector[i]  + self.dot[i] for i in range(3)]
            if self.flag_text:
                self.plots.append(ax.text(self.base.x_list[0],self.base.y_list[0],self.base.z_list[0],self.label_curve,(self.base.x_list[1],self.base.y_list[1],self.base.z_list[1]), fontsize=10))
                self.plots.append(ax.text(self.dot[0], self.dot[1], self.dot[2]+1,
                                          "{}: ({}; {}; {})".format(self.label_point, self.dot[0], self.dot[1],
                                                                    self.dot[2]), fontsize=10))
                self.plots.append(ax.text(self.dot[0]+self.vector[0],self.dot[1]+self.vector[1],self.dot[2]+self.vector[2],"{}: ({}; {}; {})".format(self.label_vector,self.vector[0], self.vector[1], self.vector[2]),(self.vector[0],self.vector[1],self.vector[2]),fontsize=10))
                self.plots.append(ax.text(-self.vector[0]*2+self.dot[0], -self.vector[1]*2+self.dot[1], -self.vector[2]*2+self.dot[2], self.label_vector,
                                          (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
            self.plots.append(ax.plot([x2,x3],[y2,y3],[z2,z3],color='green', linewidth=7))
            self.plots.append(ax.scatter(*self.dot, color='red', s=40))
            self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color='blue', linewidth=5))
            self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color=self.primitive_color, linewidth=5))

            self.plots.append(ax.plot_surface(np.array(self.x_list), np.array(self.y_list), np.array(self.z_list),label = "plot ", color=self.primitive_color, alpha=self.primitive_opacity,picker=True, zorder=1))
            canvas.draw()




        #canvas.draw()