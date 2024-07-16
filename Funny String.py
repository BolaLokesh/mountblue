#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code f
    n = len(s)
    # Create the reversed string
    rev_s = s[::-1]
    
    # Calculate differences for original string
    diffs_s = [abs(ord(s[i]) - ord(s[i+1])) for i in range(n-1)]
    
    # Calculate differences for reversed string
    diffs_rev_s = [abs(ord(rev_s[i]) - ord(rev_s[i+1])) for i in range(n-1)]
    
    # Compare the two lists of differences
    if diffs_s == diffs_rev_s:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
