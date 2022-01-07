#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    letters = set(x for x in 'abcdefghijklmnopqrstuvwxyz')
    for i in s:
        if i.lower() in letters:
            letters.remove(i.lower())
        if len(letters)==0:
            return 'pangram'
    return 'not pangram'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
