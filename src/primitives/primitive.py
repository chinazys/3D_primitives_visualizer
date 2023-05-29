class Primitive:
    """A base class representing a primitive in a three-dimensional space.

    - Attributes:
        - primitive_name (str): The name of the primitive.
        - primitive_type (str): The type of the primitive.
        - primitive_color: The color of the primitive.
        - primitive_opacity: The opacity of the primitive.
        - flag_animation: A flag indicating whether animation is enabled for the primitive.
        - flag_text: A flag indicating whether text labels are enabled for the primitive.

    - Methods:
        - build(): Build the primitive using the provided parameters.
        - update(params): Update the parameters of the primitive.
        - plot(ax, canvas, figure): Plot the primitive on the given axes, canvas, and figure.

    """
    primitive_name = None
    primitive_type = None
    primitive_color = None
    primitive_opacity = None
    flag_animation = None
    flag_text = None

    def __init__(self, params):
        """
        Initialize a Primitive object.

        - Args:
            - params (list): The parameters required to define the primitive.
        """
        self.params = params
        self.plots = []
    
    def build(self):
        """
        Build the primitive using the provided parameters.
        """
        pass

    def update(self, params):
        """
        Update the parameters of the primitive.

        - Args:
            - params (list): The updated parameters of the primitive.
        """
        self.params = params
    
    def plot(self, ax, canvas, figure):
        """
        - Plot the primitive on the given axes, canvas, and figure.

        - Args:
            - ax (Axes): The matplotlib axes object for plotting.
            - canvas (FigureCanvas): The matplotlib figure canvas object.
            - figure (Figure): The matplotlib figure object.
        """
        pass