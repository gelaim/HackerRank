#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#s: integer, starting point of Sam's house location.
#t: integer, ending location of Sam's house location.
#a: integer, location of the Apple tree.
#b: integer, location of the Orange tree.
#apples: integer array, distances at which each apple falls from the tree.
#oranges: integer array, distances at which each orange falls from the tree.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    d_a = [a]*len(apples)
    d_o = [b]*len(oranges)
    r_a = 0
    r_o = 0
    
    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <=t:
            r_a+=1
            
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            r_o+=1
    print(r_a)
    print(r_o)
    
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)