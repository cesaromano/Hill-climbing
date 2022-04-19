import matplotlib.pyplot as plt
import math
import numpy as np
import random

from hillClimbing import HillClimbing

class SimulatedAnnealing(HillClimbing):
	"""Simulated Annealing optimization class"""

	def __init__(self, p, max_it, s, g=1.0, i=0.0, f=1.0):
		"""
		Atributes initialized from the parent class
		"""
        #super().__init__(p, max_it, s, g=1.0, i=0.0, f=1.0)

