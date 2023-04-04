from primitives.primitive import Primitive
from ui.settings import AXIS_MAX_SIZE

class Line(Primitive):
    """
    Line is defined with two points, let's say A and B. To cover full canvas we may need to extend it from the both end to the canvas sizes.
    Let's say we want to extend the line from the A point side. Then out directional vector is BA(ax - bx, ay - by, az - cz).
    For each xyz coordinate of B point we build a proportional vector Ci * BA (where Ci is some scalar), so that the resulting corresponding
    coordinate is located on the canvas bounds. The minimum of the determined Ci values is used to determine the end point.
    Line extending from B point side is absolutely symmetric.
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

        if self.a_point == self.b_point:
            raise Exception("Points must be distinct")

        self.a_end_point = Line._get_end_point(self.a_point, self.b_point)
        self.b_end_point = Line._get_end_point(self.b_point, self.a_point)

    def plot(self, ax, canvas):
        try:
            ax.plot([self.a_end_point[0], self.b_end_point[0]], [self.a_end_point[1], self.b_end_point[1]], [self.a_end_point[2], self.b_end_point[2]])
            canvas.draw()
        except Exception as e:
            print(e)
