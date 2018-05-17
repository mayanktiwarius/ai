

def parseinput(input):
 items = input.split('#')
 count = int(items[0])
 minChar = items[1].split(',')
 maxChar = items[2].split(',')
 minInt = [int(x) for x in minChar]
 maxInt = [int(x) for x in maxChar]
 return count,minInt,maxInt

def maxGoal(team,maxInt):
 goal = 0
 for player in team:
  goal += maxInt[player]
 print ("Max Goal")
 print (goal)
 return goal

def minGoal(team,minInt):
 goal = 0
 #print("Min")
 #print(minInt)
 for player in team:
  goal += minInt[player]
 print ("Min Goal")
 print (goal)
 return goal

def minGoalDifference(team1,team2,minInt,maxInt):
 possibleGoalDifference = []
 print("Team1")
 print(team1)
 print("Team2")
 print (team2)
 possibleGoalDifference.append(abs(maxGoal(team1,maxInt)-minGoal(team2,minInt)))
 possibleGoalDifference.append(abs(maxGoal(team2,maxInt)-minGoal(team1,minInt)))
 #print("possibleGoalDifference")
 print(possibleGoalDifference)
 #print(min(possibleGoalDifference))
 return max(possibleGoalDifference)

def combinations(items,combo=[]):
 if combo == None:
  combo = []
 if combo.count(items) == 0:
  combo.append(items)
  combo.sort()

 for index in range(len(items)):
  #print (index)
  newList = items[:index] + items[index+1:]
  #print (newList)
  combo = combinations(newList,combo)
 return combo
 
def getAllCombinations(count):
 #print (count)
 items = [x for x in range(count)]
 #print (items)
 combo = combinations(items,None)
 del combo[0]
 return combo

def getGoals(players,teams,minInt,maxInt):
 goals = []
 print(teams)
 for team1 in teams:
  #teams.remove(team1)
  team2 = list(set(players)-set(team1))
  #teams.remove(team2)
  #print (team1)
  #print (team2)
  goals.append(minGoalDifference(team1,team2,minInt,maxInt))
 return min(goals)


if __name__ == "__main__":
 #input = "4#3,4,5,7#3,4,5,7"
 #input = "4#1,3,4,5#2,5,8,6"
 input = "3#1,3,2#4,6,5"
 count,minInt,maxInt = parseinput(input)
 #print(min)
 #print(max)
 combinations = getAllCombinations(count)
 players = [x for x in range(count)]
 #print (combinations)
 print(getGoals(players,combinations,minInt,maxInt))
 
