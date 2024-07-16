#!/bin/python3
import math
import os
import random
import re
import sys

def rev_num(n):
    return int(str(n)[::-1])

def beautifulDays(i, j, k):
    bc = 0
    for day in range(i, j + 1):
        rev_day = rev_num(day)
        if abs(day - rev_day) % k == 0:
            bc += 1
    return bc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
