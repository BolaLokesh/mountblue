#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    expected_message = "SOS";
    characters_count = 0;
    
    for i in range(0, len(s), 3):
        # comparing each segment with "SOS"
        for j in range(3):
           if s[i + j] != expected_message[j]:
            characters_count += 1
            
    return characters_count;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
