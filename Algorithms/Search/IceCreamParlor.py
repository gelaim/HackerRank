#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    adict = {}

    for i in range(len(arr)):
        if arr[i]<m and arr[i]>0:
            if arr[i] not in adict:
                adict[arr[i]] = []
            adict[arr[i]].append(i)
        if arr[i] in adict:
            if (m - arr[i]) in adict:
                if len(adict[m - arr[i]])>1:
                    return [adict[m - arr[i]][0]+1,adict[m - arr[i]][1]+1]
                if len(adict[m - arr[i]]) == 1 and 2*arr[i] != m:
                    if i < adict[m - arr[i]][0]:
                        return [i+1,adict[m - arr[i]][0]+1]
                    return [adict[m - arr[i]][0]+1,i+1]
    return [0,0]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
