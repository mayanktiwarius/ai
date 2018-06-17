hashTable = {}
hashTable['first']= 'Mayank'
hashTable['second']= 'Shivangi'
print (hashTable)
print (hashTable['first'])
try:
 print (hashTable['noKey'])
except:
 print ("Key is not found")

item = hashTable.get('first')
print (item)
item = hashTable.get('noKey')
print (item)

