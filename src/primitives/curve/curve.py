from primitives.primitive import Primitive

# simplified parametric curve (will add other then t^coef configurators late, need parser interface for that):
# curve is defined as following: x = t^a, y = t^b, z = t^c.
# a, b, c are the curve params (a corresponds to params[0], b -> params[1], c -> params[2])
class Curve(Primitive):
    def _fill_points_list(self):
        self.x_list = []
        self.y_list = []
        self.z_list = []

        for t in range(1000):
            self.x_list.append((t / 100) ** self.x_param)
            self.y_list.append((t / 100) ** self.y_param)
            self.z_list.append((t / 100) ** self.z_param)

    def build(self):
        assert len(self.params) == 3, "Curve params are invalid"

        self.x_param = self.params[0]
        self.y_param = self.params[1]
        self.z_param = self.params[2]

        self._fill_points_list()
    
    def plot(self, ax, canvas):
        try:
            ax.plot(self.x_list, self.y_list, self.z_list)
            canvas.draw()
        except:
            print('Curve is invalid => cannot plot')
