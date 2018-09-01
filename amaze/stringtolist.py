import array
data = "This is a temporary data"
print(data)
#listData = array('c',data)
#listData = array.array('u',u'hello world')
listData = array.array('u',data).reverse()
print (listData)
listData = list(data)
listData.append('\0')
print(listData)
