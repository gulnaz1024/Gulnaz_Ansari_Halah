#!/bin/python3

import math
import os
import random
import re
import sys

def best_divisor(n):
    ls = [i for i in range(1, n + 1) if n % i == 0]
    res = []
    for i in ls:
        sum = 0           
        if i > 9:
            for j in str(i):
                sum += int(j)
            res.append(sum)
        else:
            res.append(i)
            
    print(ls[res.index(max(res))])


if __name__ == '__main__':
    n = int(input().strip())
    best_divisor(n)
