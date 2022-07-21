#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    left = 0
    right = 0
    total1 = 0
    for i in range(len(arr)):
        total1+=arr[i]
    total = total1//2
    for i in range(len(arr)):
        if total1 - left -arr[i] == left:
            return 'YES'
        if left + arr[i] < total:
            left+=arr[i]
        else:
            return 'NO'
    return 'NO'
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()