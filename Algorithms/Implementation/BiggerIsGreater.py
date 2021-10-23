#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    result = 'no answer'
    alist = list(w)
    max_s = w
    i = len(alist)-1
    while i>0 and alist[i]<=alist[i-1]:
        i-=1
    i-=1    
        
    if i < 0:
        return result
    
    j = len(alist)-1
    
    while alist[j]<=alist[i]:
        j-=1
    
    
    alist[i],alist[j] = alist[j], alist[i]
    alist[i+1:]=alist[len(alist)-1:i:-1]
    
    return ''.join(alist)    
            

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
