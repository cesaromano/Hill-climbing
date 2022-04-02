import matplotlib.pyplot as plt
from function import Function
from hillClimbing import HillClimbing
import numpy as np

"""Controls the "Hill Climbing simple" algoritm using Function
    and HillClimbing classes"""

#Variable that contains a Function object, needed to plot the results
test_1 = Function()
#Variable that contains a HillClimbing object, needed to optimize the function
test_2 = HillClimbing()

#List comprehension that contains multiple multiple optimizated values 
coordinates = [test_2.optimize() for value in range(1, 11)]

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

test_1.addPointPlot(x, y)

#Plot the points on function
plt.show()