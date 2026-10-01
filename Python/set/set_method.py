'''
set.add(el)
set.remove(el)
set.clear()
set.pop()
set.copy()
set.union(set1,set2)
set.intersection(set1,set2)
set.difference(set1,set2)
'''


collection = {1,2,3,4}
collection1 = {4,5,6,7}
print(collection)
collection.add(5)
print(collection)
collection.remove(2)
print(collection)
collection.clear()
print(collection)
collection.pop()   #so as set dosen't have a order it will delete a random value
print(collection)
collection.copy()
print(collection)
collection.union(collection1)
print(collection)
collection.intersection(collection1)
print(collection)
collection.difference(collection1)
print(collection)