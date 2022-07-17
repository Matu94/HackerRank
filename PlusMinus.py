#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#Given an array of integers, calculate the ratios of its elements that 
#are positive, negative, and zero. Print the decimal value of each 
#fraction on a new line with places after the decimal.

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    pos = 0
    zer = 0
    neg = 0
    
    for i in arr:
        if i > 0 :
            pos = pos + 1
        if i == 0:
            zer = zer + 1
        if i < 0:
            neg = neg + 1
            
    print(round((pos/len(arr)),6))
    print(round((neg/len(arr)),6))
    print(round((zer/len(arr)),6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
