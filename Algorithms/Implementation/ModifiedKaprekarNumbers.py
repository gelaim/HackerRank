#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    result = []
    for i in range(p,q+1):
        n_s = i**2
        d = len(str(i))
        if len(str(n_s)) == 2*d or len(str(n_s)) == 2*d-1:
            #a = len(str(n_s)) - d
            r = int(str(n_s)[-d:])
            l = 0
            if len(str(n_s)[:-d]) >0:
                l =  int(str(n_s)[:-d])
            if r+l ==i and r >0:
                result.append(i)
    if result:
        print(*result)
    else:
        print('INVALID RANGE')
    
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

