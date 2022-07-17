#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                diag1 += arr[i][j]
            if i+j == n-1:
                diag2 += arr[i][j]
    return abs(diag1 - diag2)            
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []
    

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
