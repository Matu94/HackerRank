#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    var = n-1
    
    result = 0
    
    for i in range(n//2):
        for j in range(n//2):
            result = result + max(matrix[i][j], matrix[i][var-j], matrix[var-i][j], matrix[var-i][var-j])
    return result
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
