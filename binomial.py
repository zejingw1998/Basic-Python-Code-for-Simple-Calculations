import numpy as np
import math


def bio(n,k):
    if k < 0 or k > n:
        return 0
    k = min( k,n-k)
    res = 1
    for i in range(1,k+1):
        res = res*(n-k+i)//i
        return res
    
print(bio(5,2))

