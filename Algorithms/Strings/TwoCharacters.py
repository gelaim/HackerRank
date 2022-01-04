#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    alist = list(s)
    aset = set(alist)
    comb = combinations(list(aset),2)
    maxSize = 0
    
    for c in comb:
        currL = []
        prev = ''
        for i in alist:
            if i == c[0] and prev == c[0]:
                currL =[]
                break
            elif i == c[0] and prev == c[1]:
                currL.append(c[0])
                prev = c[0]
            elif i == c[0] and prev == '':
                prev = c[0]
                currL.append(c[0])
            elif i == c[1] and prev == c[1]:
                currL =[]
                break
            elif i == c[1] and prev == c[0]:
                currL.append(c[1])
                prev = c[1]
            elif i == c[1] and prev == '':
                prev = c[1]
                currL.append(c[1])
        maxSize = max(maxSize, len(currL))
        
    return maxSize
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
