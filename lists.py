# like an array but can be of different data types
# uses index like an array
# operations are similar to an array

#to create a list of items
items = ['names', 98.04, 21, 'i']

#to traverse a list
for item in items:
    print(item)
print()    

#to change an element at an index
items[3] = 'k'
print(items)

#to add a new element
items.insert(4," foods ")
print(items)
print()

#to remove an element at an index
items.pop(3)
print(items)

#to remove an element with value
items.remove(" foods ")
print(items)

#to search for an element in the list
print(items.index(98.04))