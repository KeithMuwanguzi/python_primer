print("Hello World")
# Variables
name = "John smith"
age = 20
is_new = True
print(name," is a new ",age," year old patient")

# Input
names = input("what is your name? ")
print("hello ", names)

#type conversion
#int(),float(),bool(),str()
birth_year=input("Enter year of birth: ")
current_age =2023- int(birth_year)
print(current_age)

# mini example
first= input("Enter first number: ")
second =input("Enter second number: ")
sum = int(first) + float(second)
print(float(sum))
#OR
first= float(input("Enter first number: "))
second =float(input("Enter second number: "))
sum = first + second
print(sum)

#strings and their operations
# upper(),lower(),find()
program =("It is software enginnerig")
print(program.upper())
print(program.find("is"))
print(program.replace("is", "was"))
print ("is" in program)

#Aritmetic operators
# x=10, x-=3(decrementing 10 by 3), x+=3(incrementing 10 by 3), x*= ......
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) # approximates
print(10  % 3) # returns reminder
print(10 ** 3) #exponential

#comparison operators
# >,>=, <, <=, ==. !=
y = 10> 2
print(y)

#logical operators
#and, or, not
price= 10
print(price > 2 and price <30)
print(price == 20 or price <3)

# conditionals.
#if
height = 7
if height > 5:
    print("she is tall")
elif height < 9:
    print("she is average height")
else:
    print("we dont know")
print("finish")    

#while
while height <= 20: 
    print(height)
    height +=1

#Lists
girls= ["joy","may","suzie","lydia", "rose"]
print(girls)
print(girls[0])
print(girls[-1])
print(girls[0: 4])
print(girls.append("mia"))
print(girls.insert(0, "kia"))
print(girls.insert(3,"lia"))
print(girls.remove("mia"))

#for loop
numbers =[1,2,3,6,8]
for item in numbers:
    print(item)

 #range functions
 #tuples.
 #are immutable
 num =(1,2,3) 
 num.count(3)
 num.index(0)

 #Dictionaries
 d1 ={1:"welcome",2:"home"}
 print(d1)

 #Sets
 s1 = set([1,2,3,5])
 s2 = set([1,8,3,7])
 print(s1.union(s2))
 
 print(s)









