import numpy as np

class Polynomial:

    def __init__(self, x: list, y: list, deg: int):
        """
        Polynomial model. 
        Attributes:
            x: list
            y: list
            deg: int
        """
        self.x = list(x)
        self.y = list(y)
        self.deg = int(deg)