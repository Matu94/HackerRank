import math
import os
import random
import re
import sys

# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, 
# just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c. 


s = 'middle-Outz'
k = 2

tmp = [0] * len(s)
result = ""

for i, value in enumerate(s):
    if value == ' ' or value == '-':
        tmp[i] = value
    else:
        tmp[i] = ord(value) + k #Get the ascii code then shift it with value "k"
        tmp[i] = chr(tmp[i])    #Get the char from ascii code
print(tmp)

for i in tmp:                   #create string from list
    result+=i
print(result)
        