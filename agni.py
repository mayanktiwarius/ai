def removeItemsFromList(items,removeItems):
 newItems = [ items[index] for index in range(len(items)) if removeItems.count(index) == 0 ]
 return newItems

def assort(items):
 area = 0
 while(len(items) != 0 or len(items) != 1):
  print ("Length is:" + str(len(items)))
  if len(items) == 1 or len(items) == 0:
   break
  lastMax = items[0]
  startIndex = 0
  endIndex = 0
  sum = items[0]
  removeItems = []
  for index in range(1,len(items)):
   print(index)
   endIndex = index
   if items[index] <= items[index-1]:
    sum += items[index]
   elif items[index] == sum:
    for i in range(startIndex,endIndex):
     removeItems.append(i)
    sum =  items[index]
    print ("Remove items")
    print(removeItems)
   else:
    for i in range(startIndex,endIndex):
     removeItems.append(i)
    sum =  sum + items[index]
    print ("Remove items")
    print(removeItems)
  area += sum
  items = removeItemsFromList(items,removeItems)
  print(items)
 return area
  

if __name__ == "__main__":
 #input = "4 2 1 4"
 #input = "4 4 4 4 8"
 #input = "4 2"
 input = "1 1 1 2"

 itemsStr = input.split(' ')
 items = [int(x)*int(x) for x in itemsStr]
 print (items)
 print(assort(items))
 #print (requiredArea(assortedItems))
