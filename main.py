from hillClimbing import HillClimbing
from simulatedAnnealing import SimulatedAnnealing
import random
import matplotlib.pyplot as plt

#Random float number betwen 0.0 and 1.0 with 2 decimal values
x = round(random.uniform(0.0, 1.0), 2)
#x = 0.1

#HillClimbing class called, first parameter: perturbation pass,
#second parameter: max iterations number
#third parameter: random samples number
#test_1 = HillClimbing(0.001, 5, 11)
#implementing hillClimbingS algoritm to object
#test_1.hillClimbingS(x)

#implementing hillClimbingI algoritm to object
#test_1.hillClimbingI(x, 2)

#implementing hillClimbingP algoritm to object
#test_1.hillClimbingP(x, 0.5)

#implementing simulatingAnneing algoritm to object
test2 = SimulatedAnnealing(50)
test2.simAnnealing(10, x, 0.7)
print(f"Random number: {x}")


plt.show()