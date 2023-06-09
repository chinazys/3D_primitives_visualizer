from primitives.primitive import Primitive
from util.expression_parser import string_to_expression, evaluate_parametric_expression, evaluate_string_numerical_expression

class Curve(Primitive):
    """A class representing a curve in three-dimensional space.
    Curve is built as a dense consequence of points, which are generated for each possible ti: xi = x(ti), yi = y(ti), zi = z(ti).
    
    - Attributes:
        - DELTA_T_MAX (float): The maximum delta t value for the curve.

    - Methods:
        - _fill_points_list(): Fills the points list of the curve.
        - contains_point(point, eps): Checks if a point lies on the curve.
        - build(): Builds the curve using the provided parameters.
        - plot(ax, canvas, figure): Plots the curve on the given axes, canvas, and figure.

    """
    DELTA_T_MAX = 1e6
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

    def contains_point(self, point, eps=1e-3):
        try:
            self.build()

            for x, y, z in zip(self.x_list, self.y_list, self.z_list):
                if abs(point.x - x) <= eps and abs(point.y - y) <= eps and abs(point.z - z) <= eps:
                    return True
            
            return False
        except:
            return True
        

    def build(self):
        assert len(self.params) == 6, "Curve params are invalid"

        self.x_string = self.params[0]
        self.y_string = self.params[1]
        self.z_string = self.params[2]
        self.t_min_string = self.params[3]
        self.t_max_string = self.params[4]

        self.x_expression = string_to_expression(self.x_string)
        self.y_expression = string_to_expression(self.y_string)
        self.z_expression = string_to_expression(self.z_string)
        self.t_min = evaluate_string_numerical_expression(self.t_min_string)
        self.t_max = evaluate_string_numerical_expression(self.t_max_string)
        self.points_quantity = int(self.params[5])

        assert self.t_min < self.t_max and self.DELTA_T_MAX > self.t_max - self.t_min, 'Invalid t limits'

        self._fill_points_list()
    
    def plot(self, ax, canvas, figure):        
        try:
            if self.flag_text:
                self.plots.append(ax.text(self.x_list[len(self.x_list) // 2], self.x_list[len(self.y_list) // 2], self.x_list[len(self.z_list) // 2], self.primitive_name, fontsize=10))

            self.plots.append(ax.plot(self.x_list, self.y_list, self.z_list, color=self.primitive_color, alpha=self.primitive_opacity))
            canvas.draw()
        except Exception as e:
            print(e)
