#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    result_r = [0]*len(container)
    result_c = [0]*len(container[0])
    
    for i, r in enumerate(container):
        result_r[i] = sum(r)
        for ic,c in enumerate(r):
            result_c[ic] +=c 
    
    if collections.Counter(result_r) == collections.Counter(result_c):
        return 'Possible'
    return 'Impossible'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
