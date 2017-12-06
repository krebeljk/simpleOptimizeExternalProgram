#!/usr/bin/env python

import subprocess as supr
import numpy as np
from scipy.optimize import minimize

# cost function
def my_run(num):
    # set parameter
    comProc = supr.run([r"sed -i 's/a\s*=\s*[^\s]*.*/a = " + str(num[0]) + "/g' calc.py"], shell=True)
    # run external program 
    comProc = supr.run([r"python calc.py"], shell=True)
    # read result
    return np.loadtxt('result.txt')

# initial guess
x0 = np.array([10])

# optimization procedure
res = minimize(my_run, x0, method='BFGS',options={'disp': True})

print(res.x)
