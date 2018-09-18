#!/bin/python3

import math
import os
import random
import re
import sys


def getAllSubsets(arr, start,end,subsets=[],subset=[]):
    #print (start,end,subset)
    if start >= end:
        subsets.append(subset[:])
        return
    for index in range(start, end+1):
        if index < end:
            subset.append(arr[index])
        getAllSubsets(arr,index+2,end,subsets,subset)
        if index < end:
            del subset[-1]

    

    

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    subsets = []
    subset = []
    getAllSubsets(arr,0,len(arr),subsets,subset)
    #print(subsets)
    maxSum = -sys.maxsize - 1
    for item in subsets:
        addItem = sum(item)
        if maxSum < addItem:
            maxSum = addItem
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

