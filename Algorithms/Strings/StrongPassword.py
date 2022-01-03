#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    hasNumber = False
    hasLower = False
    hasUpper = False
    hasSpecial = False
    
    for i in password:
        if i in numbers:
            hasNumber = True
        elif i in lower_case:
            hasLower = True
        elif i in upper_case:
            hasUpper = True
        elif i in special_characters:
            hasSpecial = True
    criteria = sum([hasNumber,hasLower,hasUpper,hasSpecial])
    if n >= 6:
        if criteria == 4:
            return 0
        else:
            return 4 - criteria
    else:
        return max(6 - n, 4 - criteria)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
