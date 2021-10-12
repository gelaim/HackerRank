#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    dist = dict()
    m = len(a)+1
    for i in range(len(a)):
        try:
            d = abs(i - dist[a[i]])
            m = min(d, m)
            
        except:
            dist[a[i]] = i
    
    if m == len(a)+1:
        return -1
    
    return m
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

