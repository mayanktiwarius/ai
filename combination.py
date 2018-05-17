def combination(list,combo=[]):
 if combo == None:
  combo = []
 if combo.count(list) == 0:
  combo.append(list)
  combo.sort()

 for index in range(len(list)):
  otherList = list[:index] + list[index+1:]
  combo = combination(otherList,combo)
 return combo 
  
if __name__ == "__main__":
 list = [1,2,3]
 combo = combination(list,None)
 del combo[0]
 print (combo)
 
