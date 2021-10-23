#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
numbers = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"
    ]
def timeInWords(h, m):
    # Write your code here
    if m ==0:
        return numbers[h] + " o' clock"
    if m ==15:
        return "quarter past " + numbers[h]
    if m == 30:
        return "half past " + numbers[h]
    if m == 45:
        return "quarter to " + numbers[h+1]
    if m ==1:
        return "one minute past " + numbers[h]
    if m == 59:
        return "one minute to " + numbers[h+1]
    if m < 30:
        return numbers[m]+" minutes past " + numbers[h]
    else:
        a = len(numbers) - m
        return numbers[a]+" minutes to " + numbers[h+1]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
