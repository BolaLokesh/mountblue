#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    n = len(s)
    
    if n == 1:
        if s[0] > 1:
            return "First"
        else:
            return "Second"
    
    all_stones_one = all(stone == 1 for stone in s)
    
    if all_stones_one:
        if n % 2 != 0:
            return "Second"
        else:
            return "First"
    
    xor_sum = 0
    for stones in s:
        xor_sum ^= stones
    
    if xor_sum == 0:
        return "Second"
    else:
        return "First"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
