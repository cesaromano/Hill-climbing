import matplotlib.pyplot as plt
import math
import numpy as np
import random

class Function:
	"""Test and plot the function and especific points"""

	def __init__(self, i=0.0, f=1.0, p=0.001):
		"""
		x: value to be evaluated
		i: range lower limit
		f: range upper limit
		p: range step 
		"""

		self.i = i
		self.f = f
		self.p = p

	def evalFunc(self, x):
		"""Evaluates the function"""
		self.x = x
		g = (2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6
		return g

	def funct(self):
		"""Return 'ax', a the subplot function in the figure"""

		values = []
		points = []

		for each in np.arange(self.i, self.f, self.p):
			test = Function.evalFunc(self, each)
			values.append(test)

		for each in np.arange(self.i, self.f, self.p):
			points.append(each)

		fig, ax = plt.subplots()
		ax.plot(points, values)
		ax.axis([0, 1.1, 0, 1.1])

		return ax

	def addPointPlot(self, px, py):
		"""Return 'ax', a subplot with the function and a especific points"""
		
		ax = Function.funct(self)
		ax.scatter(px, py, s=50)		

		return ax

	def optimizate(self, x, max_it ):
		"""Hill climbing optimization algorithm"""

		t = 1
		func = Function()
		evaluate = func.evalFunc(x)

		while (t<self.max_it and evaluate != self.g):
			
			xi = x + np.random.normal(0, 0.2, 1)
			evaluate_i = func.evalFunc(xi)
			evaluate = func.evalFunc(x)

			if evaluate_i > evaluate:
				x = xi

			t += 1

		x = x
		y = func.evalFunc(x)

		return x, y