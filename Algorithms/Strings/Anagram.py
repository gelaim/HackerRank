#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    mid = len(s)//2
    if len(s)%2 != 0:
        return -1
    
    p1 = list(s[:mid])
    p2 = list(s[mid:])
    count = 0
    for i in p1:
        if i not in p2:
            count +=1
        else:
            p2.remove(i)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
