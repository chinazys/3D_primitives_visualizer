from primitives.primitive import Primitive
from util.expression_parser import string_to_expression, evaluate_parametric_expression

# Curve is built as a dense consequence of points, which are generated for each possible ti: xi = x(ti), yi = y(ti), zi = z(ti).
class Curve(Primitive):
    plots = []

    def _fill_points_list(self):
        self.x_list = []
        self.y_list = []
        self.z_list = []

        t = self.t_min
        step = (self.t_max - self.t_min) / self.points_quantity
        while t < self.t_max:
            try:
                self.x_list.append(evaluate_parametric_expression(self.x_expression, t))
            except:
                pass

            try:
                self.y_list.append(evaluate_parametric_expression(self.y_expression, t))
            except:
                self.x_list.pop()

            try:
                self.z_list.append(evaluate_parametric_expression(self.z_expression, t))
            except:
                self.x_list.pop()
                self.y_list.pop()
            
            t += step

    def build(self):
        assert len(self.params) == 6, "Curve params are invalid"

        try:
            self.x_expression = string_to_expression(self.params[0])
            self.y_expression = string_to_expression(self.params[1])
            self.z_expression = string_to_expression(self.params[2])
            self.t_min = float(self.params[3])
            self.t_max = float(self.params[4])
            self.points_quantity = int(self.params[5])
        except:
            print('Invalid input')
            return

        assert self.t_min < self.t_max, 'Invalid t limits'
        
        self._fill_points_list()
    
    def plot(self, ax, canvas, figure):
        try:
            self.plots.append(ax.plot(self.x_list, self.y_list, self.z_list))
            canvas.draw()
        except:
            print('Curve is invalid => cannot plot')
