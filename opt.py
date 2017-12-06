#!usr/bin/env python

import subprocess as supr
import numpy as np
from scipy.optimize import minimize

def my_run(num):
    comProc = supr.run([r"sed -i 's/a\s*=\s*[0-9]*\.[0-9]*/a = " + str(num[0]) + "/g' calc.py"], shell=True)
    comProc = supr.run([r"python calc.py"], shell=True)
    return np.loadtxt('result.txt')

x0 = np.array([10])

res = minimize(my_run, x0, method='BFGS',options={'disp': True})

print(res.x)
