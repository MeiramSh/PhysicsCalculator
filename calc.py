from math import *
from numpy import *

ep = 4342342.2

def lonCapaNUmber(number):
	return format(number, '.2e').replace("e-0", "e-").replace('e+0','e').replace('e0','')

print(lonCapaNUmber(ep))