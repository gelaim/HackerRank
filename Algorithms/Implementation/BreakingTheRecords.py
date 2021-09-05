#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    cont_h = 0
    cont_l = 0
    m_h = scores[0]
    m_l = scores[0]
    for i in range(1,len(scores)):
        if scores[i]>m_h:
            cont_h +=1
            m_h = scores[i]
        elif scores[i]<m_l:
            cont_l +=1
            m_l = scores[i]
    return [cont_h, cont_l]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
