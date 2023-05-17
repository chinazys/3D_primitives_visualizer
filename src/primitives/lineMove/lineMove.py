from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.line.line import Line
import numpy as np
from matplotlib.animation import FuncAnimation



class curve_line(Primitive):

    def __init__(self, base: Curve, dot , vector):# line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)
        self.point_saved = dot
        self.vector_saved = vector
        
        self.dot = [dot.x, dot.y, dot.z]
        self.vector = [vector.x, vector.y, vector.z]
        if self.vector ==[0,0,0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(self.dot) == 3, "dot is invalid"
        assert len(self.vector) == 3, "vector is invalid"
        self.base = base
        self.base.build()

        flag = self.base.contains_point(dot)
        if not flag:
            raise Exception("curve does not contain the given point")

        self._x=[]
        self._y=[]
        self._z=[]
        self.build()
        # GENERAL PARAMETERS: are applied when plotting both animated and result surfaces
        self.ALPHA = .4  # sets capacity level
        self.DOTS = len(self.base.x_list)  # sets the number of curve dots
        self.surfaces=[]
        self.LENGTH = len(self.base.x_list)  # sets the number of dots we take from the curve to build the conical surface
        self.STEP = self.DOTS//self.LENGTH  # calculates the step of taking next dot to expand the animated conical surface
        self.TMP_RESOLUTION = 2  # number of dots each line from curve to fixdot contains
        self.PAUSE = 1  # sets pause time in seconds between fixdot, base curve and the surface plots
        self.INTERVAL = 100
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 4
        self.plots = []
        self.label_point = dot.primitive_name
        self.label_vector = vector.primitive_name
        self.label_curve = base.primitive_name
        # self.main_line = Line(dot, vector+dot)


    def build(self):
        self.x_list = [[self.base.x_list[i], self.base.x_list[i] + self.vector[0]*5] for i in range(len(self.base.x_list))]

        self.y_list = np.array(
            [[self.base.y_list[i], self.base.y_list[i] + self.vector[1] *5 ] for i in range(len(self.base.x_list))])

        self.z_list = np.array(
            [[self.base.z_list[i], self.base.z_list[i] + self.vector[2] *5] for i in range(len(self.base.x_list))])

    def plot(self, ax, canvas, fig):
            def animate(i):
                
                
                # firstly, plot the fixdot
                if i == 1:
                    if self.flag_text:
                        self.plots.append(ax.text(self.dot[0], self.dot[1], self.dot[2] + 1,
                                                  "{}: ({}; {}; {})".format(self.label_point, self.dot[0], self.dot[1],
                                                                            self.dot[2]), fontsize=10))

                    self.plots.append(ax.scatter(*self.dot, color='red', s=40))
                    canvas.draw()



                elif i == 2:
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
                elif i == 3:
                    x0, y0, z0 = [-self.vector[i] * 5 + self.dot[i] for i in range(3)]
                    x1, y1, z1 = [self.vector[i] * 5 + self.dot[i] for i in range(3)]
                    if self.flag_text:
                        self.plots.append(ax.text(-self.vector[0] * 2 + self.dot[0], -self.vector[1] * 2 + self.dot[1],
                                                  -self.vector[2] * 2 + self.dot[2], self.label_vector,
                                                  (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
                    self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color='blue', linewidth=5))
                    canvas.draw()

                    # finally, plot connecting line between P dot and fixdot
                elif i == 0:
                    if self.flag_text:
                        self.plots.append(ax.text(self.base.x_list[0], self.base.y_list[0], self.base.z_list[0],
                                                  f"{self.label_curve}",
                                                  (self.base.x_list[1], self.base.y_list[1], self.base.z_list[1]),
                                                  fontsize=10))
                    self.plots.append(
                        ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color=self.primitive_color, linewidth=5))
                    canvas.draw()

                # if it's the last dot, unite all the fragments into single surface
                elif i+1 == self.LENGTH+self.BIAS:
                    for s in self.surfaces:
                        s.remove()
                    self.plots.append(ax.plot_surface(np.array(self.x_list), np.array(self.y_list), np.array(self.z_list),label="plot ", color=self.primitive_color, alpha=self.primitive_opacity,picker=True))
                    canvas.draw()
                else:
                       
                # usually, we just add another set of dots to the list

                    self._x.append(self.x_list[(i-self.BIAS)])
                    self._y.append(self.y_list[(i-self.BIAS)])
                    self._z.append(self.z_list[(i-self.BIAS)])

                    
                    
                    if len(self._x)==2:
                        #print(self._x,self._y,self._z)
                        surf=ax.plot_surface(np.array(self._x),np.array(self._y),np.array(self._z),color=self.primitive_color,alpha=self.primitive_opacity)
                        self.surfaces.append(surf)
                        self.plots.append(surf)
                        self._x.pop(0)
                        
                        self._y.pop(0)
                        self._z.pop(0)
                        canvas.draw()
                # and if there are 2 sets of dots, we plot a surface fragment between them
                

                    
                   
                    

 

            
            # for i in range(len(self.base.x_list)):  # (change) ->   for i in range(dot P.x_param,len(self.base.x_list)):
                # ax.plot_surface(X=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]]for i in range(len(self.base.x_list))),Y=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]),Z=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]) )

                # ax.plot([self.base.x_list[i] , self.base.x_list[i] + self.vector[0]] ,[self.base.y_list[i] , self.base.y_list[i] + self.vector[1]] ,[self.base.z_list[i] , self.base.z_list[i] + self.vector[2]])
            if self.flag_animation:
                anim = FuncAnimation(fig, animate, frames=(self.LENGTH+self.BIAS) , repeat=False, interval=50, cache_frame_data=False, save_count=0)
                canvas.draw()
            else:
                x0, y0, z0 = [-self.vector[i] * 5 + self.dot[i] for i in range(3)]
                x1, y1, z1 = [self.vector[i] * 5 + self.dot[i] for i in range(3)]
                x2, y2, z2 = self.dot
                x3, y3, z3 = [self.vector[i] + self.dot[i] for i in range(3)]
                if self.flag_text:
                    self.plots.append(ax.text(self.base.x_list[0], self.base.y_list[0], self.base.z_list[0],
                                              self.label_curve,
                                              (self.base.x_list[1], self.base.y_list[1], self.base.z_list[1]),
                                              fontsize=10))
                    self.plots.append(ax.text(self.dot[0], self.dot[1], self.dot[2] + 1,
                                              "{}: ({}; {}; {})".format(self.label_point, self.dot[0], self.dot[1],
                                                                        self.dot[2]), fontsize=10))
                    self.plots.append(ax.text(self.dot[0] + self.vector[0], self.dot[1] + self.vector[1],
                                              self.dot[2] + self.vector[2],
                                              "{}: ({}; {}; {})".format(self.label_vector, self.vector[0],
                                                                        self.vector[1], self.vector[2]),
                                              (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
                    self.plots.append(ax.text(-self.vector[0] * 2 + self.dot[0], -self.vector[1] * 2 + self.dot[1],
                                              -self.vector[2] * 2 + self.dot[2], self.label_vector,
                                              (self.vector[0], self.vector[1], self.vector[2]), fontsize=10))
                self.plots.append(ax.plot([x2, x3], [y2, y3], [z2, z3], color='green', linewidth=7))
                self.plots.append(ax.scatter(*self.dot, color='red', s=40))
                self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color='blue', linewidth=5))
                self.plots.append(
                    ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color=self.primitive_color, linewidth=5))
                self.plots.append(ax.plot_surface(np.array(self.x_list), np.array(self.y_list), np.array(self.z_list), color=self.primitive_color,label="plot ", alpha=self.primitive_opacity,picker=True))

                canvas.draw()


