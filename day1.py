#variables
name = "John Smith"
age = 20
height = 45.567
new_patient = True
hobby = "swimming"
print(hobby.upper())
print(hobby.find('i'))
print('s' in hobby)
print(hobby.replace('ming','med'))
print(9/2)
print(9//2)
print(9%2)
print(name)
print(height)

#inputs.
#name = input("What is your name?\n")
#print("hello " + name)

#type conversion.
#birthYear = int(input("Which year were you born?\n"))
#age = 2023 - birthYear
#print(age)
#first = int(input("first:"))
#second = float(input("second:"))
#print("Sum: "+ str(first+second))

#conditionals
temp = 37
if temp < 37:
    print("very low")
elif temp > 37:
    print("very high")
else:
    print("very normal")


#Lists
food = ["rice","meat","gnuts","beef"]
print(food)
print(food[1])
print(food[-2])
food[0] = "chicken"
print(food[0:3])
#list methods
digits = [1,2,3,4,5,6]
digits.insert(6,7)
digits.remove(2)
#digits.clear()
print(1 in digits)
print(digits)
print (len(digits))

#loops
 #while loops
i = 1
while i<=10:
    print(i* '@')
    i = i+1
numbers = [1,2,3,4,5]

#for loops
for item in digits:
    print(item)

#range()function
numbers = range(5) #print range of numbers minus five
print(numbers)
for number in numbers:
    print(number)

digit = range(5,10)#prints numbers from 5 to 10 except 10
for num in digit:
    print (num)

numb = range(0,11,2) #2 is the step number, we skip two steps then go to the next number.
for numbe in numb:
    print(numbe)

#tuples
#these are like lists and are used to store information but they are immutable

num1 = (1,2,3,4,2,2,)
print(num1.count(2))
