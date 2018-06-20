#!/bin/python3

import math
import os
import random
import re
import sys

class Move:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cost = -1
    def setCost(self,cost):
        self.cost = cost
    def toString(self):
        #print("Test1")
        print ("X:" + str(self.x) + "Y:" + str(self.y) + ":Cost:" + str(self.cost))
        #print("Test2")


def modifyCost(currentMove):
 currentMove.cost = 10
 currentMove.toString()

if __name__ == "__main__":
 newMove = Move(5,10)
 newMove.setCost(20)
 newMove.toString()
 print("After function call")
 modifyCost(newMove)
 newMove.toString()
