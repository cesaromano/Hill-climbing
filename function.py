import matplotlib.pyplot as plt
import math
import numpy as np

class Function:
	"""Test and plot the function"""

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
		"""Plot the function"""

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

		#plot = plt.show()

		return ax

	def addPointPlot(self, px, py):
		"""Plot an especific point in the function"""
		
		ax = Function.funct(self)
		ax.scatter(px, py, s=50)		

		return ax