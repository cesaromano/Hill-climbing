import matplotlib.pyplot as plt
import math
import numpy as np

def evalFunc(x):
	"""Evaluates the function"""
	x = x
	g = (2**(-2*((x-0.1)/0.9)**2))*(math.sin(5*math.pi*x))**6
	return g

	#(2**-2((x-0.1)/0.9)**2)*(math.sin(5*math.pi*x))**6

def plotFunct(i, f, p):
	"""Plot the function"""

	values = []
	points = []

	i = i
	f = f
	p = p

	for each in np.arange(i, f, p):
		test1 = evalFunc(each)
		values.append(test1)

	for each in np.arange(i, f, p):
		points.append(each)

	fig, ax = plt.subplots()
	ax.plot(points, values)
	ax.axis([0, 1, 0, 1])

	plot = plt.show()

	return plot

plot_1 = plotFunct(0.0, 1.0, 0.001)
print(plot_1)