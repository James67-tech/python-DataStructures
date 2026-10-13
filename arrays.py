#elements in an array are of the same type and stored in a contiguous memory location
#arrays in python are dynamic ->isn't of fixed size

from array import *

#to create an array of numbers
numbers = array('I',[1,2,3,4,5])
print(type(numbers))
print(numbers)
for number in numbers:
    print(number, end=" ")
    
print()

#to return the index of an element in an array
try:
    print(numbers.index(50))
except ValueError:
    print("Not found")

print()

#to insert an element at an index
numbers.insert(5,6)
print(numbers.index(6))
print(numbers)

print()

#to delete an element 
numbers.remove(5) #pass the value
print(numbers)

print()

#to update an element at a given index
numbers[3]= 10
print(numbers)