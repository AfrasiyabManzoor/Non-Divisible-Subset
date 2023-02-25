#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    dictionary = {}
    for i in range(k):
        dictionary[i] = 0
        
    for n in s:
        dictionary[n%k] += 1
            
    print(dictionary)
    result = 0 if dictionary.get(0) == 0 else 1
    if k%2 == 0 and dictionary.get(int(k/2)) > 0:
        result += 1
    
    for i in range(1,int((k+1)/2)):
        if dictionary.get(i) > dictionary.get(k-i):
            result += dictionary.get(i)
        else: result += dictionary.get(k-i)
        
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
