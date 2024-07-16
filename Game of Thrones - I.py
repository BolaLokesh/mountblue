#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code herzx
     freq = {}
     for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Count how many characters have odd frequencies
     odd_count = 0
     for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
    
    # If more than one character has an odd frequency, it's not possible
     if odd_count > 1:
        return "NO"
     else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
