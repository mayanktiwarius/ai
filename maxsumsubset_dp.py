#!/bin/python3

import math
import os
import random
import re
import sys

class Node:    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def traverse(self):
        item = self
        while (item != None):
            print(item.data)
            item = item.next
            

        
def convertListToLinkedList(listData):
    head = None
    prev = None
    for item in listData:
        data = Node(item)
        if(head == None):
            head = data
        if(prev == None):
            prev = data
        prev.next = data
        prev = data
    return head

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
            
            
def getSumOfList(listItems):
    sum = 0
    for item in listItems:
        sum = sum + item.data
    return sum

def getMaxSubsetSum(items):
    tempHold = []
    thisItem = items
    maxSum = -sys.maxsize
    if items == None:
        return maxSum
    if items.next == None:
        return items.data
    head = items
    tempHold.append(head)
    maxSum = head.data
    currentSum = maxSum
    while (len(tempHold) != 0):
        # Add all not adjacent elements and calculate sum real time
        #print(tempHold)
        
        while tempHold[-1] != None and tempHold[-1].next != None and tempHold[-1].next.next != None:
            temp = tempHold[-1]
            tempHold.append(temp.next.next)
            currentSum = currentSum + temp.next.next.data
            if currentSum > maxSum:
                maxSum = currentSum
        #print ("After adding all altenative items")
        #print(tempHold)
        
        #Pick the last item in the stack, pop it and add all non adjacent items till then end
        #calculate maxsum real time
        temp = tempHold[-1]
        if temp.next == None:
            tempHold.pop()
            currentSum = currentSum - temp.data
            if currentSum > maxSum:
                maxSum = currentSum
        if len(tempHold) == 0:
            break
        temp = tempHold[-1]
        tempHold.pop()
        currentSum = currentSum - temp.data
        if currentSum > maxSum:
            maxSum = currentSum
        tempHold.append(temp.next)
        currentSum = currentSum + temp.next.data
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum
        
        

        
        
        
    
# Complete the maxSubsetSum function below.
def maxSubsetSum_v2(arr):
    listData = convertListToLinkedList(arr)
    #listData.traverse()
    
    
    return getMaxSubsetSum(listData)
    

# Complete the maxSubsetSum function below.
def maxSubsetSum_v1(arr):
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


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    costArr = [0] * len(arr)
    costArr[0] = arr[0]
    costArr[1] = max(arr[0],arr[1])
    for index in range(2,len(arr)):
        costArr[index] = max(costArr[index-1], costArr[index-2] + arr[index])
    return costArr[len(costArr) -1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

