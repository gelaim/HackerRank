#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    result = []
    for i in grid:
        result.append(list(i))
    for r in range(1, len(result)-1):
        for c in range(1,len(result[r])-1):
            curr = result[r][c]
            if result[r-1][c] < curr and result[r+1][c]<curr and result[r][c+1] < curr and result[r][c-1]<curr:
                result[r][c]='X'
    r_result = []
    for v in result:
        r_result.append(''.join(v))
    return r_result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
