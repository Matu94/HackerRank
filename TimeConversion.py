#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 

def timeConversion(s):
    # Write your code here
    
    h=int(s[0:2]) 
    if s[-2]=='P':
        if h!=12:
            h=12+h
        else:
            h=h    
        return(str(h)+s[2:8])
    else:
        if h==12:
            return("00"+s[2:8])
        else:
            return(s[:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
