#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    area = len(A)*len(A[0])*2
    
    dp = [[0]*(len(A[0])+2)]
    
    for row in A:
        dp.append([0]+row+[0])
    dp.append([0]*(len(A[0])+2))
    
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            area += abs(dp[i][j] - dp[i-1][j])
            area += abs(dp[i][j] - dp[i][j-1])

            
            
    return area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

