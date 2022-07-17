#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    n = n+1
    for i in range(n):
        if i == 0:
            continue
        if (i%3 == 0) and (i%5 == 0):
            print("FizzBuzz")
        if (i%3 == 0) and (i%5 != 0):
            print("Fizz")
        if (i%3 != 0) and (i%5 == 0):
            print("Buzz")    
        if (i%3 != 0) and (i%5 != 0):
            print(i)
    
if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)
