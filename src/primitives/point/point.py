from primitives.primitive import Primitive

class Point(Primitive):
    def build(self):
        self.x = float(self.params[0])
        self.y = float(self.params[1])
        self.z = float(self.params[2])