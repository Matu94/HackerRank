#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given a list of integers, count and return the number of times each value appears as an array of integers.
#

def countingSort(arr):
    # Write your code here
    m=[]
        
    for i in range(100):
        if i in arr:
            m.append(arr.count(i))
        else:
            m.append(0)
    return m
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
