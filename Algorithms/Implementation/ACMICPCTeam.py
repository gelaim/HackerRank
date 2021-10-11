#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    n_max = 0
    count = 0
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            c1 = int(topic[i],2)
            c2 = int(topic[j],2)
            curr = str(bin(c1|c2)).count('1')
            if curr == n_max:
                count +=1
            elif curr > n_max:
                count = 1
                n_max = curr
    return [n_max, count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
