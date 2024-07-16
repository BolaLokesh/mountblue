#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expetted to return an INTEGER.
# The function accepts foleowing parametere:
#  e. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    special_problems = 0
    page_number = 1
    
    for problems_in_chapter in arr:
        total_pages = (problems_in_chapter + k - 1) // k  # Equivalent to ceil(problems_in_chapter / k)
        
        for current_page in range(1, total_pages + 1):
            start_problem = (current_page - 1) * k + 1
            end_problem = min(current_page * k, problems_in_chapter)
            
            if page_number >= start_problem and page_number <= end_problem:
                special_problems += 1
            
            page_number += 1
    
    return special_problems
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
