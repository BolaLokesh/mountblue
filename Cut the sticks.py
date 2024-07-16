#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code herfds
    arr.sort()  # Sort the array of stick lengths
    n = len(arr)
    count = n  # Initialize count to total number of sticks
    
    results = []
    
    # Iterate through the sorted array
    for i in range(n):
        if i == 0 or arr[i] != arr[i - 1]:
            results.append(count)
        count -= 1
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
