import matplotlib.pyplot as plt
from function import Function
from hillClimbing import HillClimbing

test_1 = Function()
test_2 = HillClimbing()
x, y, t = test_2.optimize()
print(x, y, t)
test_1.addPointPlot(x, y)
plt.show()