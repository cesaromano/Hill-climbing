from hillClimbing import HillClimbing
import random
import matplotlib.pyplot as plt

#Random float number betwen 0.0 and 1.0 with 2 decimal values
x = round(random.uniform(0.0, 1.0), 2)

#HillClimbing class called, first parameter: perturbation pass,
#second parameter: max iterations number
test_1 = HillClimbing(0.001, 40)
#implementing hillClimbingS algoritm to object
test_1.hillClimbingS(x)

plt.show()