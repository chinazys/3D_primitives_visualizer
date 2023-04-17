from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.line.line import Line
import numpy as np




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
        # self.main_line = Line(dot, vector+dot)


    def build(self):
        pass

    def plot(self, ax, canvas):


            x=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0]] for i in range(len(self.base.x_list))])


            y = np.array([[self.base.y_list[i], self.base.y_list[i] + self.vector[1]] for i in range(len(self.base.x_list))])

            z = np.array([[self.base.z_list[i], self.base.z_list[i] + self.vector[2]] for i in range(len(self.base.x_list))])

            Z = np.outer(z, np.ones_like(x))
            # for i in range(len(self.base.x_list)):  # (change) ->   for i in range(dot P.x_param,len(self.base.x_list)):
                # ax.plot_surface(X=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]]for i in range(len(self.base.x_list))),Y=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]),Z=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]) )
                # ax.plot([self.base.x_list[i] , self.base.x_list[i] + self.vector[0]] ,[self.base.y_list[i] , self.base.y_list[i] + self.vector[1]] ,[self.base.z_list[i] , self.base.z_list[i] + self.vector[2]])
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X,Y,Z)

            canvas.draw()


