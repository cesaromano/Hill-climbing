import matplotlib.pyplot as plt
from function import Function
from hillClimbing import HillClimbing

test_1 = Function()
test_2 = HillClimbing()
print(test_2.optimize())
#test_1.addPointPlot()
plt.show()