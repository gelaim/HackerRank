#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    alist = list(s)
    

    while len(alist)>0:
        prev = alist[0]
        cont = 1
        result = []        
        for i in range(1, len(alist)):
            if alist[i]==prev:
                cont+=1
            else:
                if cont %2 != 0:
                    result.append(alist[i-1])
                cont = 1
                prev = alist[i]
        else:
            if len(alist)>0 and cont%2!= 0:
                result.append(alist[-1])
        if len(alist) == 0:
            return 'Empty String'                    
        if len(alist) == len(result):
            return ''.join(result)
        else:
            alist = result            
            
    return 'Empty String'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

