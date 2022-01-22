#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    cont = 0
    contests = list(reversed(sorted(contests,key=lambda x:x[0])))
    print(contests)
    result = 0
    for c in contests:
        if cont < k and c[1]==1:
            cont+=1
            #print(c[0])
            result+= c[0]
        elif c[1]==0:
            result +=c[0]
        else:
            result -=c[0]
                    

    return result        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
