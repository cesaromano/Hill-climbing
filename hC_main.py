import matplotlib.pyplot as plt
from function import Function
from hillClimbing import HillClimbing
import numpy as np

test_1 = Function()
test_2 = HillClimbing()

coordinates = [test_2.optimize() for value in range(1, 11)]

x = [coordinates[value][0] for value in range(0, len(coordinates))]
x = np.asfarray(x)
y = [coordinates[value][1] for value in range(0, len(coordinates))]
y = np.asfarray(y)

#px = [value for value in np.arange(0.1, 1.0, 0.1)]
#py = [value for value in np.arange(0.1, 1.0, 0.1)]


print(x, y)

#x, y, t, r, le = test_2.optimize()
#print(x, y, t, r, le)
test_1.addPointPlot(x, y)
plt.show()