#!usr/bin/env python

import subprocess as sp
import numpy as np

a = 3.2
com = "echo " + str(a**2) + " > result.txt"

sp.run(com, shell=True)
