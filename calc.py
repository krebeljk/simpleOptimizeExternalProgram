#!/usr/bin/env python

import subprocess as sp
import numpy as np

# input param
a = 7.8
# computation
com = "echo " + str(a**2) + " > result.txt"
# result export
sp.run(com, shell=True)
