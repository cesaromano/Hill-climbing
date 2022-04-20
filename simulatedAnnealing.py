import matplotlib.pyplot as plt
import math
import numpy as np
import random

from hillClimbing import HillClimbing

class SimulatedAnnealing(HillClimbing):
	"""Simulated Annealing optimization class"""

	
	def __init__(self, max_it, g=0.1, i=0.0, f=1.0, p=0.001):
		"""
		Atributes initialized from the parent class
		"""

		self.max_it = max_it
		self.g = g
		self.i = i
		self.f = f
		self.p = p


	def simAnnealing(self, T, x, B):
		"""
		Controls the "Simulated Annealing" algoritm using
    	HillClimbing classes
		"""

		evaluate = super().evalFunc(x)

		t = 1
		xil = []
		xa = []

		while (t<self.max_it and x != self.g):
			xi = x + np.random.normal(0.0, 0.02, 1)
			#xil.append(xi)
			evaluate_i = super().evalFunc(xi)
			evaluate = super().evalFunc(x)

			if evaluate_i > evaluate:
				x = xi
			elif round(random.uniform(0.0, 1.0), 2) < math.exp((evaluate_i-evaluate)/T):
				x = xi
			
			T = B * T

			#xa.append(x)

			t += 1

		y = super().evalFunc(x)
		print(f"x:{x}, y:{y} \nTemperature:{T}\nIterations: {t}\nPerturbations: {xil}\nx acepted: {xa}")

		plot = super().addPointPlot(x, y)

		return plot