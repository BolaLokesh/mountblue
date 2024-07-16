#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    # Flags for checking if password contains required character types
    has_digit = has_lower = has_upper = has_special = False
    
    # Check each character in the password to set the flags
    for char in password:
        if char in numbers:
            has_digit = True
        elif char in lower_case:
            has_lower = True
        elif char in upper_case:
            has_upper = True
        elif char in special_characters:
            has_special = True
    
    # Count missing types
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1
    
    # Calculate the number of characters needed to reach minimum length
    min_length_needed = max(0, 6 - n)
    
    # The answer is the maximum of missing types or length difference
    return max(missing_types, min_length_needed)
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
