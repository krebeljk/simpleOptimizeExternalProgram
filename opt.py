#!usr/bin/env python

import subprocess as sp
import numpy as np

comProc = sp.run([r"sed -i 's/a\s*=\s*[0-9]*\.[0-9]*/a = 7.8/g' calc.py"], shell=True)
comProc = sp.run([r"python calc.py"], shell=True)

result = np.loadtxt('result.txt')
print(result)
