import numpy as np
import math
from math import exp, sqrt


def find_root(a,b,c):
    D = b**2-4*a*c
    if D < 0:
        raise ValueError("This equation have not reell rot")
    root_1 =(-b+np.sqrt(D))/(2*a)
    root_2 =(-b-np.sqrt(D))/(2*a) 
    return root_1,root_2
a=6
b=5
c=1

print(find_root(a,b,c))

