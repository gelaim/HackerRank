#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    result = []
    position = 1
    ranked = list(set(ranked))
    ranked.sort(reverse = True)
    player.sort(reverse = True)
    k = 0
    for i in range(len(player)):
        if ranked[-1] > player[i]:
            result.insert(0,len(ranked)+1)
        else:
            while player[i] < ranked[k] and k < len(ranked)-1:
                k+=1
                position+=1
            
            result.insert(0,position)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

