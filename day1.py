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
birthYear = int(input("Which year were you born?\n"))
age = 2023 - birthYear
print(age)
first = int(input("first:"))
second = float(input("second:"))
print("Sum: "+ str(first+second))

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


#dictionaries
#allow us to work with key value pairs
student = {'name':'Martha', 'age':30,'location':'Mbarara','hobbies':['eating','sleeping']}
print(student)
print(student['name'])
print(student['hobbies'])
print(student.get('class'))#we use .get function inorder not to get the error message if we accessed a none existent key
del student['age']
print(student)
student.update({'name':'Keith','location':'Kampala','hobbies':['ball','code']})
print(len(student))
print(student.values())
print(student.items())

#looping through dicts
for key, values in student.items():
    print(key, values)


#sets
#a collection of data with no duplicates.
num2 = [1,2,3,3,4,3,3]
#to convert it to a set
first = set(num2)
second = {6,7,3,1}
print(first | second)#for union sets
print(first & second)#for intersection
print(first - second)#for first only
print(first ^ second)# elements in either ets but not both
#we dont access items by index in a set because its unordered
if 9 in first
    print("yes")
else:
    print("no")

