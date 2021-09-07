#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    result = 0
    cont = 1
    prev= ar[0]
    for i in range(1,len(ar)):
        if ar[i]==prev:
            if cont == 1:
                result +=1
                cont = 0
            else:
                cont+=1
        else:
            cont =1
        prev = ar[i]
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

