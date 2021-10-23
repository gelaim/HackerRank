#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    n_pages = 0
    count = 0
    for i in range(0, n):
        n_problems = 0
        while n_problems < arr[i]:
            n_pages+=1
            if n_pages in range(n_problems+1, min(n_problems+k+1, arr[i]+1) ):
                count +=1
            n_problems = min(n_problems + k, arr[i])
    return count   
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
