#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    n_prev = 0
    n_cur = 1
    cur = a[0]
    result = 0
    for i in range(1,len(a)):
        if cur == a[i]:
            n_cur +=1
            result = max(result, n_cur+n_prev)
        elif cur+1 == a[i]:            
            n_prev = n_cur
            n_cur = 1
            result = max(result, n_cur+n_prev)
            cur = a[i]

        else:
            n_prev = 0
            n_cur = 1
            cur = a[i]
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
