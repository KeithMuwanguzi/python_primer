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

i = 1
while i<=10:
    print(i* '@')
    i = i+1

#Lists
food = ["rice","meat","gnuts","beef"]
print(food)
print(food[1])
print(food[-2])
food[0] = "chicken"
print(food[0:3])
#list methods
digits = [1,2,3,4,5,6]
digits.insert(7)