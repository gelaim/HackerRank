#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    target = arr[-1]

    for i in range(len(arr)-2,-1,-1):
        if arr[i]>target:
            arr[i+1] = arr[i]
            r = ' '.join(str(x) for x in arr)
            print(r)
        else:
            arr[i+1]=target
            r = ' '.join(str(x) for x in arr)
            print(r)
            break
    if arr[0]>target:
        arr[0]=target
        r = ' '.join(str(x) for x in arr)
        print(r)   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
