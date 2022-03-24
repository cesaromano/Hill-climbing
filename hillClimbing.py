import math
import numpy as np
from function import Function
import random

class HillClimbing:
    """Hill climbing optimization method"""

    def __init__(self, max_it=1000, g=1.0):
        """
        max_it: maximum iteration number
        g: optimal point
        """

        self.max_it = max_it
        self.g = g

    def optimize(self):
        """Hill climbing optimization algorithm"""

        t = 1
        x = round(random.uniform(0.0, 1.0), 1)

        test_1 = Function()
        evaluate = test_1.evalFunc(x)

        while t<self.max_it and evaluate!=self.g:

            xi = x + np.random.normal(0, 0.1, 1)
            test_2 = Function()
            evaluate_i = test_2.evalFunc(xi)

            if evaluate_i > evaluate:
                evaluate = evaluate_i
            
            t += 1
            
        return xi, evaluate