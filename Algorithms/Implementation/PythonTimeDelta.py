#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    #Sun 10 May 2015 13:54:36 -0700
    #%a = Abbrev weekday name
    #%d = day of the month
    #%b = abbrev month
    #%Y = year
    #%z = utc zone
    fmt = '%a %d %b %Y %H:%M:%S %z'
    a = dt.strptime(t1, fmt)
    b = dt.strptime(t2, fmt)
    result = int(abs(a - b).total_seconds())
    return str(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

