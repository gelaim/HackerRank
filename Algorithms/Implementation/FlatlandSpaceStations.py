#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_d = c[0]
    for i in range(0, len(c)-1):
        max_d = max(abs(c[i]-c[i+1])//2,max_d)
        
    max_d = max(abs(n-1 - c[-1]),max_d)
    return max_d
    
        
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

