import array 
# from array import * >> create an array as array()   >>>>another way to import array
#import array as arr >> creates an array as arr.array() >>>>another way to import array
#Arrays.
 #for integers , i
numbers = array.array('i', [10,20,30])
print(numbers)
for number in numbers:
    print(number)

#floating numbers, d
more = array.array('d',[2.7,40.8, 7.0,5.0])
print(more)
print(len(more)) #aray lenghth.
#Accessing individual array items.
print(more[2])
# Searching through an array
print(more.index(40.8))
#slicing and array
print(more[:2])
print(more[1:4])
print(more[2:3])
#changing value of an item in array.
more[1]=20.0
print(more)
#adding a new value on the array.
numbers.append(50)
print(numbers)
#adding items at the end of array.
numbers.extend([45,67,89])
print(numbers)
#adding items at the beggining of array.
numbers.insert(0,68)
print(numbers)
#removing numbers.
numbers.remove(50)
print(numbers)

numbers.pop(2)
print(numbers)