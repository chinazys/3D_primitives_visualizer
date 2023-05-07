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
        self.plane = []
        # self.main_line = Line(dot, vector+dot)


    def build(self):
        self.x_list = [[self.base.x_list[i], self.base.x_list[i] + self.vector[0] * 20] for i in range(len(self.base.x_list))]

        self.y_list = np.array(
            [[self.base.y_list[i], self.base.y_list[i] + self.vector[1] * 20] for i in range(len(self.base.x_list))])

        self.z_list = np.array(
            [[self.base.z_list[i], self.base.z_list[i] + self.vector[2] * 20] for i in range(len(self.base.x_list))])

    def plot(self, ax, canvas, fig, _color):





            # for i in range(len(self.base.x_list)):  # (change) ->   for i in range(dot P.x_param,len(self.base.x_list)):
                # ax.plot_surface(X=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]]for i in range(len(self.base.x_list))),Y=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]),Z=np.array([[self.base.x_list[i] , self.base.x_list[i] + self.vector[0] ]for i in range(len(self.base.x_list))]) )
                # ax.plot([self.base.x_list[i] , self.base.x_list[i] + self.vector[0]] ,[self.base.y_list[i] , self.base.y_list[i] + self.vector[1]] ,[self.base.z_list[i] , self.base.z_list[i] + self.vector[2]])

            self.plots.append(ax.plot(self.base.x_list,self.base.y_list,self.base.z_list))
            self.plots.append(ax.plot(self.x_list[0], self.y_list[0], self.z_list[0]))
            self.plots.append(ax.plot_surface(self.x_list,self.y_list,self.z_list,color=_color))


            canvas.draw()


