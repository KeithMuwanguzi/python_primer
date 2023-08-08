# function without parameters
def dance():
    print("we are dancing salsa today")

dance()

#with arguments
def add(a, b):
    print(a+b)
add(2,4) 

#with return statement.
def multiply(num):
    return num* 4
result = multiply(5)
print(result)   

def addnum(x:int, y:int):
    z=x+y
    return z
x,y=10,5
sum =addnum(x,y)
print(f"The sum of {x} and {y} is {sum}")    

#built in functions.
print(bin(3))
name=['jose','himh','joy','cane']
print(list(enumerate(name)))