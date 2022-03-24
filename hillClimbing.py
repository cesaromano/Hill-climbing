import math
import numpy as np
from function import Function
import random

class HillClimbing:
    """Hill climbing optimization method"""

    def __init__(self, max_it, g=(0.1, 1.0)):
        """
        max_it: maximum iteration number
        g: optimal point
        """

        self.max_it = max_it
        self.g = g

    def optimize(self):
        """Hill climbing optimization algorithm"""

        t = 1
        x = random(0.0, 1.0)

        test_1 = Function()
        evaluate = test_1.evalFunc(x)

        while t<self.max_it and (x, evaluate)!=self.g: 
            print("a")
            
        return 