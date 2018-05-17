def permute(list):
 if len(list) == 0:
  return None
 if len(list) == 1:
  return [list]

 permute_list = []
 for element in list:
  remaining_element = [x for x in list if x != element]
  remaining_permute = permute(remaining_element)
  #print ("Remaining permute:" )
  #print ( remaining_permute)
  for item in remaining_permute:
   #print("Element:" + element)
   #print("Item:" )
   #print(item)
   permute_list.append([element] + item)
 return permute_list


if __name__ == "__main__":
  #list = ['0','1','2','3','4']
  #list = ['a','b','c','d','e','f','g','h','i']
  list = [0,1,2]
  print (permute(list))
 
