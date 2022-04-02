import math
import numpy as np
from function import Function
import random

class HillClimbing:
    """Hill climbing optimization method"""

    def __init__(self, max_it=2, g=1.0):
        """
        max_it: maximum iteration number
        g: optimal point
        """

        self.max_it = max_it
        self.g = g

    def optimize(self):
        """Hill climbing optimization algorithm"""

        t = 1
        x = round(random.uniform(0.0, 1.0), 2)
        #x = 0.3
        r = x

        func = Function()
        evaluate = func.evalFunc(x)

        le = []

        while (t<self.max_it and evaluate!=self.g):

            xi = x + np.random.normal(0, 0.05, 1)
            evaluate_i = func.evalFunc(xi)
            evaluate = func.evalFunc(x)

            if evaluate_i > evaluate:
                x = xi

            #if t>11:
                #print("error")
                #break
            
            t += 1
            le.append(x)
        
        x = x
        y = func.evalFunc(x)
        #y = y[0]

        #return x, y, t, r, le
        return x, y