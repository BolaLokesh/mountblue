#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) //2
    s1 = s[:mid]
    s2 = s[mid:]
    c1 = [0] * 26
    c2 = [0] * 26
    for char in s1:
        c1[ord(char) - ord('a')] += 1
        
    for char in s2:
        c2[ord(char) - ord('a')] += 1
        
        
    change = 0
    for i in range(26):
        change += abs(c1[i] - c2[i])
    return change // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
