import matplotlib.pyplot as plt
import math
import numpy as np
import random

from hillClimbing import HillClimbing

class SimulatedAnnealing(HillClimbing):
	"""Simulated Annealing optimization class"""

	
	def __init__(self, max_it):
		#"""
		#Atributes initialized from the parent class
		#"""
		super().__init__(max_it)

		#self.B = B

	def simAnnealing(self, T, x, B):
		"""
		Controls the "Simulated Annealing" algoritm using
    	HillClimbing classes
		"""

		evaluate = super().evalFunc(self, x)

		t = 1

		while (t<self.max_it and evaluate != self.g):
			xi = x + np.random.normal(0, 0.2, 1)
			evaluate_i = super().evalFunc(self, xi)

			if evaluate_i > evaluate:
				x = xi
			elif round(random.uniform(0.0, 1.0), 2) < math.exp((evaluate_i-evaluate)/T):
				x = xi
			
			T = B * T

			t += 1

		y = super().evalFunc(self, x)
		print(x, y)

		plot = super().addPointPlot(self, x, y)

		return plot