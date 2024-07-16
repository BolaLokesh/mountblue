#!/bin/python3

import math
import os
import random
import re
import sys

def minimumDistances(a):
    index_map = {}
    min_distance = float('inf')
    
    for i in range(len(a)):
        num = a[i]
        if num in index_map:
            indices = index_map[num]
            
            prev_index = indices[-1]
            distance = i - prev_index
            
            if distance < min_distance:
                min_distance = distance
            
            indices.append(i)
        else:
            
            index_map[num] = [i]
    
    return -1 if min_distance == float('inf') else min_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
