def initialize_array():
 array1 = [1,2,3]
 array2 = [3,4,5]
 print("Inside the function")
 print (array1)
 print (array2)
 return array1,array2

if __name__ == "__main__":
 array1 = []
 array2 = []
 array1, array2 = initialize_array()
 print (array1)
 print (array2)
 list = [0,1,2,3,4,5]
 print (list[:2])
 print (list[3:])
 list = [0]
 print (list[:0])
 list = [-13,13]
 print min(list)
