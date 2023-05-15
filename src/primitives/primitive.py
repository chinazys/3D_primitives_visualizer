class Primitive:
    primitive_name = None
    primitive_type = None
    primitive_color = None
    primitive_opacity = None
    flag_animation = None
    flag_text = None

    def __init__(self, params):
        self.params = params
        self.plots = []
    
    def build(self):
        pass

    def update(self, params):
        self.params = params
    
    def plot(self, ax, canvas, figure):
        pass