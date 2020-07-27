#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minStart' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
    
def minStart(arr):
    # Write your code here

    newArr = [] * len(arr) 
    newElem = 0

    for i in range(len(arr)): 
        newElem += arr[i]
        newArr.append(newElem)
    
    sol = min(newArr)

    solu = abs(sol) + 1 

    solution = int(solu)    
    
    return solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minStart(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
