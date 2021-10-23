#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import zip_longest
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace('\s', '')
    floor = math.floor(math.sqrt(len(s)))
    ceil = math.ceil(math.sqrt(len(s)))
    min_a = floor*floor
    r = floor
    c = floor
    while min_a <len(s):
        if r==c:
           c+=1
        else:
           r+=1
        min_a = r*c
    m = []
    
    for i in range(0,len(s),c):
        m.append(s[i:i+c])
    return ' '.join([''.join(x) for x in list(zip_longest(*m, fillvalue=''))])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
