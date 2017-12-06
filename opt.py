#!usr/bin/env python

import subprocess as supr
import numpy as np

def my_run(num):
    comProc = supr.run([r"sed -i 's/a\s*=\s*[0-9]*\.[0-9]*/a = " + str(num) + "/g' calc.py"], shell=True)
    comProc = supr.run([r"python calc.py"], shell=True)
    return np.loadtxt('result.txt')

my_run(30.1)
