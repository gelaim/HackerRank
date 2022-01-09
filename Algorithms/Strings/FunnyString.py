#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    t = [ord(x) for x in s]
    tl = []
    ul = []
    n = len(t)-1
    for i in range(len(t)-1):
        tl.append(abs(t[i]-t[i+1]))
        ul.append(abs(t[n-i]-t[n-i-1]))
    if ul ==tl:
        return 'Funny'
    return 'Not Funny'

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
