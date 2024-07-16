#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    
    for length in range(1, n // 2 + 1):
        sn = int(s[:length])
        cn = sn
        cs = ""
        
        while len(cs) < n:
            cs += str(cn)
            cn += 1
        
        if cs == s:
            print(f"YES {sn}")
            return
    
    print("NO")
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
