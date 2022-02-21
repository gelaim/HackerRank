#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    #https://www.youtube.com/watch?v=3BaZ3SkTfc0
    number_inversions = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                number_inversions +=1
    if number_inversions%2==0:
        return 'YES'
    return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()

