#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code her
     kaprekar_nums = []
    
     for num in range(p, q + 1):
        square = num * num
        str_square = str(square)
        
        # Split into two parts
        d = len(str(num))
        right_part = int(str_square[-d:]) if str_square[-d:] else 0
        left_part = int(str_square[:-d]) if str_square[:-d] else 0
        
        # Check if it's a Modified Kaprekar Number
        if left_part + right_part == num:
            kaprekar_nums.append(num)
    
     if kaprekar_nums:
        print(" ".join(map(str, kaprekar_nums)))
     else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
