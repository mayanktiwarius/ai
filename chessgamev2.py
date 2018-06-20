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
        return maxMoves
    for move in moves:
        if move.cost > maxCost:
            #maxMove = move
            maxCost = move.cost
    maxMoves =[ move for move in moves if move.cost == maxCost]
    return maxMoves

def getMin(moves):
    minMove = None
    minCost = 10 # As maximum value of cost is 4
    minMoves = []
    if moves == None:
        return minMoves
    for move in moves:
        if move.cost < minCost:
            #minMove = move
            minCost = move.cost 
    minMoves = [ move for move in moves if move.cost == minCost]
    return minMoves

def printMoves(moves):
    print ("Moves possible:")
    if moves == None:
        return
    for move in moves:
        move.toString()

def getBestMove(currentMove, maxStrategy, level):
    print ("getBestMove")
    currentMove.toString()
    #if level == 3:
    #    currentMove.setCost(moveCost(currentMove))
    #    return currentMove
    moves = []
    movePossible = False
    if inrange(currentMove.x-2) and inrange(currentMove.y+1):
        newMove = Move(currentMove.x-2,currentMove.y+1)
        newMove, nextMove = getBestMove(newMove,not(maxStrategy),level+1)  
        if( nextMove != None):
            movePossible = True
            print("next move calculated")
            nextMove.toString()
            newMove.cost = nextMove.cost
            moves.append(newMove)
    if inrange(currentMove.x-2) and inrange(currentMove.y-1):
        newMove = Move(currentMove.x-2,currentMove.y-1)
        newMove, nextMove = getBestMove(newMove,not(maxStrategy),level+1)
        if(nextMove != None):
            movePossible = True
            print("next move calculated")
            nextMove.toString()            
            newMove.cost = nextMove.cost
            moves.append(newMove)
    if inrange(currentMove.x+1) and inrange(currentMove.y-2):
        newMove = Move(currentMove.x+1,currentMove.y-2)
        newMove,nextMove = getBestMove(newMove,not(maxStrategy),level+1)
        if(nextMove != None):
            movePossible = True
            print("next move calculated")
            nextMove.toString()            
            newMove.cost = nextMove.cost
            moves.append(newMove)
    if inrange(currentMove.x-1) and inrange(currentMove.y-2):
        newMove = Move(currentMove.x-1,currentMove.y-2)
        newMove, nextMove = getBestMove(newMove,not(maxStrategy),level+1)
        if(nextMove != None):
            movePossible = True
            print("next move calculated")
            nextMove.toString()            
            newMove.cost = nextMove.cost
            moves.append(newMove)
    if not movePossible:
        currentMove.cost = 0
        return currentMove, currentMove
    
    currentMove.cost = len(moves)
    print ("Modified current move")
    currentMove.toString()
        
    print ("Checking moves from:" )
    currentMove.toString()
    printMoves(moves)
    if maxStrategy:
        newMoves = getMax(moves)
        if (newMoves != None and len(newMoves) >= 1):
            return currentMove, newMoves[0]
        else:
            return None
        #print ("Max move is:")
        #newMove.toString()
        #return newMove
    else:
        newMoves = getMin(moves)
        if (newMoves != None and len(newMoves) >= 1):
            return currentMove,  newMoves[0]
        else:
            return None
    

    

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    moveCount = 0
    #if move count is odd then it was player 1 move else it was player 2 move
    thisMove = Move(x,y)
    while True:
        moveCount+=1 
        print("Main")
        thisMove, newMove = getBestMove(thisMove,False,0)
        if  newMove == thisMove:
            print("New move is none")
            break
        else :
            thisMove =  newMove
            print ("New move is:")
            print (thisMove.toString())
            #print ("Test3" + str(moveCount))
            #if moveCost of new move is 0 this means that next player cant move anymore
            if moveCost(thisMove) == 0 :
                #print("Breaking form the loop")
                #moveCount+=1
                break
    if moveCount % 2 == 0:
        print ("Second")
        return "Second"
    else:
        print ("First")
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

