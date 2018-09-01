
def computeDays(values,days):
 for day in range(days):
  newValues = []
  for index in range(len(values)):
   print("Index is:" + str(index))
   left = 0
   right = 0
   if index == 0:
    left = 0
   else:
    left = values[index-1]
   if index == len(values) -1 :
    right = 0
   else: 
    right = values[index+1]
   print("Left is: " + str(left))
   print("Right is: " + str(right))
   newValues.append(computeSingle(left,right))
   print (newValues)
  print(newValues)
  values = newValues
 return values


def computeSingle(item1, item2):
 return item1 ^ item2


if __name__ == '__main__':
 values = [1,0,0,0,0,1,0,0]
 days = 2
 newValues = computeDays(values,days)
 print(newValues)
