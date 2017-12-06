#!usr/bin/env python

import subprocess as sp
import numpy as np

num = 12.2

comProc = sp.run([r"sed -i 's/a\s*=\s*[0-9]*\.[0-9]*/a = " + str(num) + "/g' calc.py"], shell=True)
comProc = sp.run([r"python calc.py"], shell=True)

result = np.loadtxt('result.txt')
print(result)
