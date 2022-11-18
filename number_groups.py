#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumOfGroup' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#


def sumOfGroup(k):
     
    firstEl = int((k * (k - 1)) + 1)
    sum = 0
     
    while k:
        sum += firstEl
        firstEl += 2
        k=k-1
     
    return sum
     
k=3
print(sumOfGroup(k))

if name == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    answer = sumOfGroup(k)

    fptr.write(str(answer) + '\n')

    fptr.close()
