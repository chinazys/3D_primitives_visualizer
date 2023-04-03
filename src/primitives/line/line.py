from primitives.primitive import Primitive

# simplified parametric curve (will add other then t^coef configurators late, need parser interface for that):
# curve is defined as following: x = t^a, y = t^b, z = t^c.
# a, b, c are the curve params (a corresponds to params[0], b -> params[1], c -> params[2])
class Line(Primitive):
    def build(self):
        assert len(self.params) == 2, "Line params are invalid"

        self.start_point = self.params[0]
        self.end_point = self.params[1]

        (self.x1, self.y1, self.z1) = self.start_point
        (self.x2, self.y2, self.z2) = self.end_point

    def plot(self, ax, canvas):
        try:
            ax.plot([self.x1, self.x2], [self.y1, self.y2], [self.z1, self.z2])
            canvas.draw()
        except:
            print('Curve is invalid => cannot plot')
