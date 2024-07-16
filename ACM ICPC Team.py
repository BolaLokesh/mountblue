#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code 
    n = len(topic)
    m = len(topic[0])
    
    max_top = 0
    max_cnt = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            i_s = set(index + 1 for index, value in enumerate(topic[i]) if value == '1')
            j_s = set(index + 1 for index, value in enumerate(topic[j]) if value == '1')
            
            kn_top = len(i_s | j_s)
            
            if kn_top > max_top:
                max_top = kn_top
                max_cnt = 1
            elif kn_top == max_top:
                max_cnt += 1
    return [max_top,max_cnt];

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
