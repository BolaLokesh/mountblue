#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    common_length = 0
    min_length = min(len(s), len(t))
    
    # Calculate the length of common prefix
    for i in range(min_length):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    
    delete_ops = len(s) - common_length
    append_ops = len(t) - common_length
    
    if k >= len(s) + len(t):
        return "Yes"
    elif k >= delete_ops + append_ops and (k - delete_ops - append_ops) % 2 == 0:
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
