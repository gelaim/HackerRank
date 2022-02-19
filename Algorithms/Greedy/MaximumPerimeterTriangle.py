#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def findLongest(A,B,C):
    longest = max(A+B, B+C)
    longest = max(A+C, longest)
    return longest    

def findMinimum(A,B,C):
    longest = min(A+B, B+C)
    longest = min(A+C, longest)
    return longest    
    

def maximumPerimeterTriangle(sticks):
    # Write your code here
    #A + B > C and B + C > A and C + A > B 
    result = [-1]
    sticks.sort()
    for i in range(2,len(sticks)):
        A = sticks[i-2]
        B = sticks[i-1]
        C = sticks[i]
        if A + B > C and B + C > A and C+A >B:
            if len(result) == 1:
                result = [A,B,C]
                continue
            if  A+B+C < sum(result):
                continue
            elif A + B + C > sum(result):
                result=[A,B,C]
                continue                
            curr_longest = findLongest(A,B,C)
            result_longest = findLongest(result[0],result[1],result[2])
            if curr_longest > result_longest:
                result = [A,B,C]
                continue
            elif curr_longest == result_longest:
                curr_min = findMinimum(A,B,C)
                result_min = findMinimum(result[0],result[1],result[2])
                if curr_min < result_min:    
                    result = [A,B,C]
                    continue
    return result
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

