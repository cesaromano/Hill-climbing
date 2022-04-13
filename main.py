from hillClimbing import HillClimbing
import random
import matplotlib.pyplot as plt

#Random float number betwen 0.0 and 1.0 with 2 decimal values
x = round(random.uniform(0.0, 1.0), 2)

#HillClimbing class called, first parameter: perturbation pass,
#second parameter: max iterations number
#third parameter: random samples number
test_1 = HillClimbing(0.001, 5, 11)
#implementing hillClimbingS algoritm to object
#test_1.hillClimbingS(x)

#implementing hillClimbingI algoritm to object
#test_1.hillClimbingI(x, 2)

#implementing hillClimbingP algoritm to object
test_1.hillClimbingP(x, 0.5)

plt.show()