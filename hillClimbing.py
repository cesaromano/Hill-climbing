import math
import numpy as np
from function import Function
import random

class HillClimbing:
    """Hill climbing optimization class"""

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
        #Random number to be evaluated
        x = round(random.uniform(0.0, 1.0), 2)
        #Fixed number to be evaluated
        #x = 0.3

        #Control variable to see the random number given
        r = x

        #Instantiate a Function object, in order to evaluate a given nnumber
        func = Function()
        evaluate = func.evalFunc(x)

        #Control variable to see the variable climbing history
        le = []

        while (t<self.max_it and evaluate!=self.g):

            xi = x + np.random.normal(0, 0.05, 1)
            evaluate_i = func.evalFunc(xi)
            evaluate = func.evalFunc(x)

            if evaluate_i > evaluate:
                x = xi
            
            t += 1
            le.append(x)
        
        x = x
        y = func.evalFunc(x)

        #Return coordinates and control variables
        #return x, y, t, r, le
        #Return coordinates only
        return x, y