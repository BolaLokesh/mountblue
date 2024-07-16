#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    position = {arr[i]: i for i in range(n)}
    largest_value = n
    i = 0
    
    while k > 0 and i < n:
        if arr[i] != largest_value:
            
            current_index = i
            max_index = position[largest_value]
            
          
            position[arr[current_index]] = max_index
            position[arr[max_index]] = current_index
            
            
            arr[current_index], arr[max_index] = arr[max_index], arr[current_index]
            
            
            k -= 1
        
        
        i += 1
        largest_value -= 1
    
    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()