import matplotlib.pyplot as plt
from function import Function
from hillClimbing import HillClimbing
import numpy as np

m = 0
t = 1
n_start = 2
g = 1.0

func = Function()

while (t<n_start and func.evalFunc(m)!=g):
    a