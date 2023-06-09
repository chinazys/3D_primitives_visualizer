from primitives.primitive import Primitive
from ui.settings import AXIS_MAX_SIZE

class Line(Primitive):
    """A class representing a line in three-dimensional space.
    Line is defined with two points, let's say A and B. To cover full canvas we may need to extend it from the both end to the canvas sizes.
    Let's say we want to extend the line from the A point side. Then out directional vector is BA(ax - bx, ay - by, az - cz).
    For each xyz coordinate of B point we build a proportional vector Ci * BA (where Ci is some scalar), so that the resulting corresponding
    coordinate is located on the canvas bounds. The minimum of the determined Ci values is used to determine the end point.
    Line extending from B point side is absolutely symmetric.
    
    - Methods:
        - _get_multiplier(directional_coor, anchor_coor): Calculate the multiplier for extending the line.
        - _get_end_point(directional_point, anchor_point): Calculate the end point of the line.
        - build(): Build the line using the provided parameters.
        - plot(ax, canvas, figure): Plot the line on the given axes, canvas, and figure.

    """
    def _get_multiplier(directional_coor, anchor_coor):
        if directional_coor == 0:
            return 1e9 # cannot extend with this coordinate => return infinity
        
        if directional_coor < 0:
            return (-AXIS_MAX_SIZE - anchor_coor) / directional_coor
        else:
            return (AXIS_MAX_SIZE - anchor_coor) / directional_coor

    def _get_end_point(directional_point, anchor_point):
        directional_vector = (directional_point[0] - anchor_point[0], directional_point[1] - anchor_point[1], directional_point[2] - anchor_point[2])
        
        multiplier = min([Line._get_multiplier(directional_vector[i], anchor_point[i]) for i in range(3)])
        end_point = (anchor_point[0] + directional_vector[0] * multiplier, 
                     anchor_point[1] + directional_vector[1] * multiplier, 
                     anchor_point[2] + directional_vector[2] * multiplier)
        
        return end_point

    def build(self):
        assert len(self.params) == 2, "Line params are invalid"

        self.a_point = self.params[0]
        self.b_point = self.params[1]

        if self.a_point.x == self.b_point.x and self.a_point.y == self.b_point.y and self.a_point.z == self.b_point.z:
            raise Exception("Points must be distinct")

        self.a_end_point = Line._get_end_point([self.a_point.x, self.a_point.y, self.a_point.z], [self.b_point.x, self.b_point.y, self.b_point.z])
        self.b_end_point = Line._get_end_point([self.b_point.x, self.b_point.y, self.b_point.z], [self.a_point.x, self.a_point.y, self.a_point.z])

    def plot(self, ax, canvas, figure):
        try:
            a_label = "{}: ({}; {}; {})".format(self.a_point.primitive_name, self.a_point.x, self.a_point.y, self.a_point.z)
            self.plots.append(ax.scatter(self.a_point.x, self.a_point.y, self.a_point.z, s=15, color=self.primitive_color))
            if self.flag_text:
                self.plots.append(ax.text(self.a_point.x + 3, self.a_point.y + 3, self.a_point.z + 3, a_label, fontsize=10))

            b_label = "{}: ({}; {}; {})".format(self.b_point.primitive_name, self.b_point.x, self.b_point.y, self.b_point.z)
            self.plots.append(ax.scatter(self.b_point.x, self.b_point.y, self.b_point.z, s=15, color=self.primitive_color))
            if self.flag_text:
                self.plots.append(ax.text(self.b_point.x + 3, self.b_point.y + 3, self.b_point.z + 3, b_label, fontsize=10))

            if self.flag_text:
                name_x, name_y, name_z = (self.a_point.x + self.b_point.x) / 3, (self.a_point.y + self.b_point.y) / 3, (self.a_point.z + self.b_point.z) / 3
                name_direction = (self.b_point.x - self.a_point.x, self.b_point.y - self.a_point.y, self.b_point.z - self.a_point.z)
                self.plots.append(ax.text(name_x, name_y, name_z, self.primitive_name, name_direction, fontsize=10))
            
            self.plots.append(ax.plot([self.a_end_point[0], self.b_end_point[0]], [self.a_end_point[1], self.b_end_point[1]], [self.a_end_point[2], self.b_end_point[2]], color=self.primitive_color, alpha=self.primitive_opacity))
            canvas.draw()
        except Exception as e:
            print(e)
