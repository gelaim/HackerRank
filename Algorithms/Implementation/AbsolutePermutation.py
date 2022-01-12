#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        return [x for x in range(1, n+1)]
    if 2*k >n:
        return [-1]
    elif n%(2*k)!=0:
        return [-1]
    pos = []
    for i in range(1,n+1):
        if ((i-1)//k)%2==0:
            pos.append(i+k)
        else:
            pos.append(i-k)
            
    if len(set(pos))<n:
        return[-1]
    return pos
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

