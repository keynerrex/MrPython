class Color:
    def __init__(self, color):
        self._color = color

    @property
    def get_color(self):
        return f"Color: {self._color} "

    @get_color.setter
    def set_color(self, color):
        self._color = color

    def __str__(self):
        return f"Color: color:[{self._color}]"
