#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    adict = {}
    prev = s[0]
    cont = ord(s[0])-96
    adict[cont] = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            cont += ord(s[i])-96
            if cont not in adict:
                adict[cont] = s[i]
        else:
            prev = s[i]
            cont = ord(s[i])-96
            if cont not in adict:
                adict[cont] = s[i]
    result = []
    for i in queries:
        if i in adict:
            result.append('Yes')
        else:
            result.append('No')
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

