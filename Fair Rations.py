#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code hv
    total_loaves = 0
    N = len(B)
    
    for i in range(N - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            total_loaves += 2
    
    # Check if all subjects have even loaves
    if all(b % 2 == 0 for b in B):
        return str(total_loaves)
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
