import matplotlib.pyplot as plt
import math
import numpy as np

class HillClimbing:
	"""Hill climbing optimization class"""

	def __init__(self, p, max_it, g=1.0, i=0.0, f=1.0):
		"""
		x: value to be evaluated
		i: range lower limit
		f: range upper limit
		p: range step 
		max_it: iteration number
		"""

		self.i = i
		self.f = f
		self.p = p
		self.max_it = max_it
		self.g = g

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
			test = HillClimbing.evalFunc(self, each)
			values.append(test)

		for each in np.arange(self.i, self.f, self.p):
			points.append(each)

		fig, ax = plt.subplots()
		ax.plot(points, values)
		ax.axis([0, 1.1, 0, 1.1])

		return ax

	def addPointPlot(self, px, py):
		"""Return 'ax', a subplot with the function and a especific points"""
		
		ax = HillClimbing.funct(self)
		ax.scatter(px, py, s=50)		

		return ax

	def optimizate(self, x):
		"""Hill climbing optimization algorithm"""

		t = 1

		#Instantiate a Function object, in order to evaluate a given nnumber
		evaluate = HillClimbing.evalFunc(self, x)

		#Control variable to see the variable climbing history
        #le = []

		while (t<self.max_it and evaluate != self.g):
			
			xi = x + np.random.normal(0, 0.2, 1)
			evaluate_i = HillClimbing.evalFunc(self, xi)
			evaluate = HillClimbing.evalFunc(self, x)

			if evaluate_i > evaluate:
				x = xi

			t += 1
			#le.append(x)

		x = x
		y = HillClimbing.evalFunc(self, x)

		#Return coordinates and control variables
		return x, y

	def hillClimbingS(self, x):
		"""
		Controls the "Hill Climbing simple" algoritm using Function
    	and HillClimbing classes
		"""

		#List comprehension that contains multiple multiple optimizated values 
		coordinates = [HillClimbing.optimizate(self, x) for value in range(1, 11)]

		#List comprehension that contain the 'x' coordinates
		x = [coordinates[value][0] for value in range(0, len(coordinates))]
		x = np.asfarray(x)

		#List comprehension that contain the 'y' coordinates
		y = [coordinates[value][1] for value in range(0, len(coordinates))]
		y = np.asfarray(y)

		#Contain one optimizated value
		#x, y, t, r, le = test_2.optimize()

		#Show coordinates and control variables	
		#print(x, y, t, r, le)	

		plot = HillClimbing.addPointPlot(self, x, y)

		return plot

	def hillClimbingI(self, x, n_start):
		"""
		Controls the "Iterated Hill Climbing" algoritm using Function
    	and HillClimbing classes
		"""

		best = 0.0
		t = 1

		while (t<n_start and best != self.g):
			
			#evaluate = HillClimbing.evalFunc(self, x) 

			x = HillClimbing.optimizate(self, x)
			x = x[0]
			t += 1		

			if x > best:
				best = x

		y = HillClimbing.evalFunc(self, x)
		print(x, y)

		plot = HillClimbing.addPointPlot(self, x, y)

		return plot