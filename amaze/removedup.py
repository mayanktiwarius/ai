import array
data = "This string may have duplicate characters"

def getArray(t):
  s = array.array('u', t)
  s.append('\0')
  return s

def removeDuplicate(s1):
 s = list(s1)
 s.append('\0')
 print(s)
 hashSet = set()
 readIndex = 0
 writeIndex = 0
 while s[readIndex] != '\0':
  if s[readIndex] not in hashSet:
   hashSet.add(s[readIndex])
   s[writeIndex] = s[readIndex]
   writeIndex+=1
  readIndex+=1
 s[writeIndex] = '\0'
 print(s)
 index = 0
 s2 = list()
 while (s[index] != '\0'):
  s2.append(s[index])
  index += 1
  
 s2.append('\0')
 s1 = ''.join(s2)

 print(s1)
 return s1

print(removeDuplicate(data))
  
 

