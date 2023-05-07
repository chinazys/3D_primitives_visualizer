class Primitive:
    primitive_name = None
    primitive_type = None
    
    def __init__(self, params):
        self.params = params
        self.plots = []
    
    def build(self):
        pass

    def update(self, params):
        self.params = params
    
    def plot(self, ax, canvas, figure):
        pass