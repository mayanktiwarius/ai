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

        

def inrange(item):
    if(item >=1 and item <=15):
        return True
    return False
    
    
def moveCost(move):
    x = move.x
    y = move.y
    cost = 0
    if inrange(x-2) and inrange(y+1):
        cost+=1
    if inrange(x-2) and inrange(y-1):
        cost+=1
    if inrange(x+1) and inrange(y-2):
        cost+=1
    if inrange(x-1) and inrange(y-2):
        cost+=1
    return cost

def getMax(moves):
    maxMove = None
    maxCost = -1
    maxMoves = []
    if moves == None:
        return maxMove
    for move in moves:
        if move.cost > maxCost:
            maxMove = move
            maxCost = move.cost
    #maxMoves =[ move for move in moves if move.cost == maxCost]
    #return maxMoves
    return maxMove

def getMin(moves):
    minMove = None
    minCost = 10 # As maximum value of cost is 4
    minMoves = []
    if moves == None:
        return minMove
    for move in moves:
        if move.cost < minCost:
            minMove = move
            minCost = move.cost 
    #minMoves = [ move for move in moves if move.cost == minCost]
    #return minMoves
    return minMove

def printMoves(moves):
    print ("Moves possible:")
    if moves == None:
        return
    for move in moves:
        move.toString()
def getAllMoves(currentMove):
    newMoves = []
    if inrange(currentMove.x-2) and inrange(currentMove.y+1):
        newMove = Move(currentMove.x-2,currentMove.y+1)
        newMoves.append(newMove)

    if inrange(currentMove.x-2) and inrange(currentMove.y-1):
        newMove = Move(currentMove.x-2,currentMove.y-1)
        newMoves.append(newMove)

    if inrange(currentMove.x+1) and inrange(currentMove.y-2):
        newMove = Move(currentMove.x+1,currentMove.y-2)
        newMoves.append(newMove)

    if inrange(currentMove.x-1) and inrange(currentMove.y-2):
        newMove = Move(currentMove.x-1,currentMove.y-2)
        newMoves.append(newMove)
    return newMoves

    
    

def getBestMove(currentMove, maxStrategy, level):
    #print("CurrentMove is : level" + str(level))
    #currentMove.toString()
    #if level == 4:
    #   currentMove.setCost(moveCost(currentMove))
    #    print("CurrentMove after setting cost is:")
    #    currentMove.toString()
    #    return None
    newMoves = getAllMoves(currentMove)
    #print("New Moves possible:")
    #printMoves(newMoves)
    for newMove in newMoves:
        getBestMove(newMove, not maxStrategy,level+1)
    #print("New Moves after setting cost:")
    #printMoves(newMoves)
    if maxStrategy:
        bestMove = getMax(newMoves)
        if bestMove == None:
            currentMove.setCost(-1)
    else:
        bestMove = getMin(newMoves)
        if bestMove == None:
            currentMove.setCost(10)

    if bestMove != None :
        #print ("Best move is:")
        #bestMove.toString()
        currentMove.setCost(bestMove.cost)
    else:
        #print("Best move is none")
        
    return bestMove

    

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    moveCount = 0
    #if move count is odd then it was player 1 move else it was player 2 move
    thisMove = Move(x,y)
    while True:
        moveCount+=1 
        #print("Main")
        thisMove =  getBestMove(thisMove,True,0)
        if thisMove == None:
            #No new move possible no point in checking further
            #Previous player is the winner
            #print("Best move returned is None")
            moveCount+=1
            break
    if moveCount % 2 == 0:
        #print ("Second")
        return "Second"
    else:
        #print ("First")
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()

