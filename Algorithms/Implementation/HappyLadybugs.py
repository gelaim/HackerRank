#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    count = Counter(b)

    sum_elements = 0
    for i in count.most_common():
        if i[0] == '_':
            continue
        elif i[1] == 1:
            return 'NO'
        sum_elements+=i[1]
                
    if sum_elements < len(b):           
        return 'YES' 
    for i,v in enumerate(b):
        if i >0 and i < len(b)-1:
            if b[i] != b[i-1] and b[i]!= b[i+1]:
                return 'NO'
            
             
    return 'YES'    
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
