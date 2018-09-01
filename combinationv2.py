def comparator(x):
 return len(x) 
def combination(list,combo=[]):
 if len(list) == 0:
  return combo
 if combo.count(list) == 0:
  combo.append(list)

 for index in range(len(list)):
  otherList = list[:index] + list[index+1:]
  combo = combination(otherList,combo)
 return combo 
  
if __name__ == "__main__":
 list = [1,2,3,1]
 combo = []
 combo = combination(list,combo)
 print (combo)
 combo.sort()
 print (combo)
 combo.sort(reverse=True)
 print (combo)
 print (sorted(combo,key=comparator))
 combo.sort(key=comparator,reverse=True)
 print (combo)
 
