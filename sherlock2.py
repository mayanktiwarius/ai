#!/bin/python3

import math
import os
import random
import re
import sys

anagramDictionary = dict()
def sortString(item):
 return ''.join(sorted(item))

def precheck(item1, item2):
 myset1 = set()
 myset2 = set()
 for item in item1:
  myset1.add(item)
 for item in item2:
  myset2.add(item)
 myset3 = myset1.intersection(myset2)
 if len(myset3) == len(myset2):
  return True
 #print ("Precheck failed for : " + str(item1) + ":" + str(item2))
 return False
 
def isAnagram(item1, item2):
 if (not precheck(item1, item2)):
  return False
 sItem1 = sortString(item1)
 sItem2 = sortString(item2)
 key = sItem1+sItem2
 
 if key in anagramDictionary:
  return True
 if sortString(item1) == sortString(item2):
  anagramDictionary[key] = 1
  return True
 return False

NO_OF_CHARS = 256
def isAnagram2(item1,item2):
 key = item1+item2
 if key in anagramDictionary:
  return True
 tracker = [0] * NO_OF_CHARS
 for character in item1:
  tracker[ord(character)] += 1
 for character in item2:
  tracker[ord(character)] -= 1
  if (tracker[ord(character)]) < 0:
   return False
 anagramDictionary[key] = 1
 return True
 


def getAllSubstringsOfSize(string,size):
 if size > len(string):
   return None
 listOfStrings = []
 for start in range(0,len(string)-size+1):
   #print ("Loop")
   listOfStrings.append(string[start:start+size])
 return listOfStrings
 
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
 #print(s)
 #for item in s:
 # print (item)
 #print (sortString(s))
 #if (isAnagram(s,s)):
 #  print ("Is anagram")

 countTracker = dict()
 anagramCounter = 0
 #print(getAllSubstringsOfSize(s,2))
 for size in range(1,len(s)):
   items = getAllSubstringsOfSize(s,size)
   for i in range (0,len(items)-1):
    item = sortString(items[i])
    if item not in countTracker:
     countTracker[item] = 0
    for j in range (i+1, len(items)):
     item = sortString(items[j])
     if item in countTracker:
      countTracker[item] += 1
     else:
      countTracker[item] = 0

 for key in countTracker:
  anagramCounter += countTracker[key]

 #print("Anagram Counter is :" + str(anagramCounter))
 #print(countTracker)
 print(str(anagramCounter))
 return anagramCounter

    
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
