#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    important_contests = []
    total_luck = 0
    
    for luck, importance in contests:
        if importance == 0:
            
            total_luck += luck
        else:
            
            important_contests.append(luck)
    
    
    important_contests.sort(reverse=True)
    
    
    for i in range(min(k, len(important_contests))):
        total_luck += important_contests[i]
    
  
    for i in range(min(k, len(important_contests)), len(important_contests)):
        total_luck -= important_contests[i]
    
    return total_luck
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
