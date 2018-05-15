import math
class Classified:
 def __init__(self,temp,bp,category):
  self.temp = int(temp)
  self.bp = int(bp)
  self.category = category
 def __str__(self):
  return str(self.temp) + ',' + str(self.bp) + ',' + self.category
  

def distance (item1, item2):
 #distance1 = 0
 distance1 = pow(item1.temp-item2.temp,2) + pow(item1.bp-item2.bp,2)
 print ("Distance finction called")
 print (distance1)
 return distance1

def parse_input(input):
 classified = []
 items = []
 existing_data, new_data = input.split('#')
 print (existing_data)
 print (new_data)
 e_datas = existing_data.split(',')
 for e_data in e_datas:
  data = e_data.split(' ')
  classify = Classified(data[0],data[1],data[2])
  classified.append(classify)
 n_datas = new_data.split(',')
 for n_data in n_datas:
  data = n_data.split(' ')
  item = Classified(data[0],data[1],"Unknown")
  items.append(item)

 for classify in classified:
  print (classify)
 for item in items:
  print (item)
 return classified, items

def classify(classified,items):
 print ("Classify function called")
 #distance_vector = [(distance(classier, item) for classier in classified) for item in items]
 #distance_vector = [distance(classier,item) for classier in classified for item in items if classier != item]
 distance_vector = [[]]
 #for classify in classified:
 # for item in items:
 #  distance(classify,item)
 #print (distance_vector)
 for item in items:
  distance_list = []
  for classify in classified:
   distance_list.append(distance(classify,item))
  distance_vector.append(distance_list)
  
 del distance_vector[0]

 print (distance_vector)
 return distance_vector

def print_classification(classified,distance_vector):
 output = ''

 for list in distance_vector:
  minimum = (list.index(min(list)))
  print (minimum)
  indexes = [index for index in range(len(list)) if list[index] == list[minimum]]
  print (indexes)
  if len(indexes) == 1:
   print (classified[indexes[0]].category)
   output+= classified[indexes[0]].category + ' '
  else:
   print ("Unknown")
   output+= "Unknown "
 print ("output is:")
 print (output)
  

  
 

if __name__ == "__main__":
 #input = "90 120 Infected,90 150 NotInfected,100 140 Infected,80 130 NotInfected#95 125,95 145,75 160"
 input = "80 120 Infected,70 145 Infected,90 100 Infected,80 150 NotInfected,80 80 NotInfected,100 120 NotInfected#120 148,75 148,60 90"
 #classified, items = parse_input(input)
 classified, items = parse_input(input)
 distance_vector = classify(classified,items)
 print_classification(classified,distance_vector)

