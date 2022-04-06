from hillClimbing import HillClimbing
import random
import matplotlib.pyplot as plt

x = round(random.uniform(0.0, 1.0), 2)

test_1 = HillClimbing()
test_1.hillClimbingS(x)


plt.show()