from primitives.curve.curve import Curve
from primitives.line.line import Line
from primitives.primitive import Primitive

class LineByCurve(Primitive):
    def __init__(self, curve: Curve, line: Line):
        self.curve = curve
        self.line = line

    def plot(self, ax, canvas):
        try:
            self.curve.build()
            self.line.build()
            for i in range(len(self.curve.x_list)):
                ax.plot([self.curve.x_list[i], self.curve.x_list[i] + self.line.b_end_point[0]], \
                         [self.curve.y_list[i], self.curve.y_list[i] + self.line.b_end_point[1]], \
                           [self.curve.z_list[i], self.curve.z_list[i] + self.line.b_end_point[2]])
            canvas.draw()
        except:
            print('Surface is invalid => cannot plot')