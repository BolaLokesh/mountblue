#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
     arr.sort()
    
    # Initialize the minimum difference as a large number
     md = float('inf')
    
    # Iterate through the sorted array and find the minimum difference
     for i in range(len(arr) - 1):
         d = abs(arr[i] - arr[i + 1])
         if d < md:
            md = d
    
     return md

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
