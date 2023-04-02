class Primitive:
    def __init__(self, params):
        self.params = params
    
    def build(self):
        pass

    def update(self, params):
        self.params = params
    
    def plot(self, ax, canvas):
        pass

    def dispose(self):
        pass