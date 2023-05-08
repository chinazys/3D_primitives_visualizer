from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.line.line import Line
import numpy as np
from matplotlib.animation import FuncAnimation



class curve_line(Primitive):
    def dot_in_curve(self):
        if self.dot in [[self.base.x_list[i], self.base.y_list[i],self.base.z_list[i]] for i in range(len(self.base.x_list))]:
            pass
        else:
            raise Exception('Dot not in Curve')
    def __init__(self, base: Curve, dot : list, vector : list):# line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)
        if vector ==[0,0,0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(dot) == 3, "dot is invalid"
        assert len(vector) == 3, "vector is invalid"
        self.base = base
        self.base.build()
        self.dot=dot
        curve_line.dot_in_curve(self)
        self.vector=vector
        self._x=[]
        self._y=[]
        self._z=[]
        self.build()
        # GENERAL PARAMETERS: are applied when plotting both animated and result surfaces
        self.ALPHA = .4  # sets capacity level
        self.DOTS = len(self.base.x_list)  # sets the number of curve dots

        self.LENGTH = len(self.base.x_list)//2  # sets the number of dots we take from the curve to build the conical surface
        self.STEP = self.DOTS//self.LENGTH  # calculates the step of taking next dot to expand the animated conical surface
        self.TMP_RESOLUTION = 2  # number of dots each line from curve to fixdot contains
        self.PAUSE = 1  # sets pause time in seconds between fixdot, base curve and the surface plots
        self.INTERVAL = 100
        # bias is required because during first several frames we build fixdot, base curve, P dot and connecting line
        self.BIAS = 3
        self.plots = []
        # self.main_line = Line(dot, vector+dot)


    def build(self):
        self.x_list = [[self.base.x_list[i], self.base.x_list[i] + self.vector[0] * 20] for i in range(len(self.base.x_list))]

        self.y_list = np.array(
            [[self.base.y_list[i], self.base.y_list[i] + self.vector[1] * 20] for i in range(len(self.base.x_list))])

        self.z_list = np.array(
            [[self.base.z_list[i], self.base.z_list[i] + self.vector[2] * 20] for i in range(len(self.base.x_list))])

    def plot(self, ax, canvas, fig, _color):
            
            def animate(i):
                
                
                # firstly, plot the fixdot
                if i == 0:
                    
                    self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list, color='green', linewidth=5))
                    canvas.draw()
                    return                
                    
                # next, plot the base curve                
                elif i == 1:
                    
                    self.plots.append(ax.scatter(*self.dot, color='red', s=40))
                    canvas.draw()
                    return
                    
                # finally, plot connecting line between P dot and fixdot
                elif i == 2:
                    x0, y0, z0 = self.dot
                    x1, y1, z1 = [self.vector[i]+self.dot[i] for i in range(3) ]
                    self.plots.append(ax.plot([x0, x1], [y0, y1], [z0, z1], color=_color, linewidth=5))
                    canvas.draw()
                    self.INTERVAL = 100
                    return
                # if it's the last dot, unite all the fragments into single surface
                elif i == self.LENGTH+self.BIAS:
                    self._x.append(self.x_list[-1])
                    self._y.append(self.y_list[-1])
                    self._z.append(self.z_list[-1])
                    self.plots.append(ax.plot_surface(np.array(self._x),np.array(self._y),np.array(self._z),color=_color,alpha=0.4))
                    canvas.draw()
                else:
                       
                # usually, we just add another set of dots to the list
                    try:
                        self._x.append(self.x_list[(i-self.BIAS)*4])
                        self._y.append(self.y_list[(i-self.BIAS)*4])
                        self._z.append(self.z_list[(i-self.BIAS)*4])
                    except:
                        return
                    
                    
                    if len(self._x)==2:
                        #print(self._x,self._y,self._z)
                        self.plots.append(ax.plot_surface(np.array(self._x),np.array(self._y),np.array(self._z),color=_color))
                        self._x.pop(0)
                        
                        self._y.pop(0)
                        self._z.pop(0)
                        canvas.draw()
                # and if there are 2 sets of dots, we plot a surface fragment between them
                

                    
                   
                    

 

            
            # for i in range(len(self.base.x_list)):  # (change) ->   for i in range(dot P.x_param,len(self.base.x_list)):
                # ax.plot_surface(X=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]]for i in range(len(self.base.x_list))),Y=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]),Z=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]) )
                # ax.plot([self.base.x_list[i] , self.base.x_list[i] + self.vector[0]] ,[self.base.y_list[i] , self.base.y_list[i] + self.vector[1]] ,[self.base.z_list[i] , self.base.z_list[i] + self.vector[2]])
            anim = FuncAnimation(fig, animate, frames=(self.LENGTH+self.BIAS) , repeat=False, interval=50, cache_frame_data=False, save_count=0)
            #self.plots.append(ax.plot(self.base.x_list,self.base.y_list,self.base.z_list))
            #self.plots.append(ax.plot(self.x_list[0], self.y_list[0], self.z_list[0]))
            #self.plots.append(ax.plot_surface(self.x_list,self.y_list,self.z_list,color=_color))


            canvas.draw()


