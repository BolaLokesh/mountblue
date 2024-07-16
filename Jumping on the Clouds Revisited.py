#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0  # Start at the first cloud

    while True:
        # Jump to the next cloud
        i = (i + k) % n
        energy -= 1  # Reduce energy by 1 for the jump
        if c[i] == 1:
            energy -= 2  # Reduce additional 2 energy if it's a thunderhead
        
        if i == 0:
            break  # If we're back to the starting point, stop the loop
    
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
