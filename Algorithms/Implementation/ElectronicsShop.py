#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()
    if b < keyboards[0]+ drives[0]:
        return -1
    result = 0
    for i in range(len(keyboards)-1, -1, -1):
        if keyboards[i]> b:
            continue
        curr = 0
        print(keyboards[i])
        for j in range(len(drives)-1,-1,-1):
            if drives[j]+keyboards[i]>b:
                continue
            curr = drives[j]+keyboards[i]
            break
        result = max(curr, result)        
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
