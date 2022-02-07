#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def createGrid(gridList, rows, columns):
    nextGrid = [['O']*columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if gridList[i][j]=='O':
                nextGrid[i][j]='.'
                up = i-1
                down = i+1
                left = j-1
                right = j+1
                if up >=0:
                    nextGrid[up][j]='.'
                if down < rows:
                    nextGrid[down][j]='.'
                if left >=0:
                    nextGrid[i][left]='.'
                if right < columns:
                    nextGrid[i][right]='.' 
    return nextGrid
def bomberMan(n, grid):
    # Write your code here
    rows = len(grid)
    columns = len(grid[0])
    gridList = []
    result = []

    if n%2 ==0:
        return ['O'*columns for _ in range(rows)]

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(grid[i][j])
        gridList.append(row) 
        
    if n == 1:
        l = []
        for i in gridList:
            row = ''.join(i)
            l.append(row)
        return l   
    first = createGrid(gridList,rows,columns)

    if n < 4:
        l = []
        for i in first:
            row = ''.join(i)
            l.append(row)
        return l    
    second = createGrid(first, rows, columns)
    third = createGrid(second, rows, columns)
    if n%4 ==1:
        
        r = []
        for i in second:
            l = ''.join(i)
            r.append(l)
        return r

    r = []
    for i in third:
        l = ''.join(i)
        r.append(l)
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
