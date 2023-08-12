print("----------calculator application in python----------")
#functions for the calculations.
def add(n,m):
    return n+m

def subtract(n,m):
    return n-m

def multiply(n,m):
    return n*m

def divide(n,m):
    return n/m    
#choices for user.
print("Please select a choice\n")
print("1, Add")
print("2, Subtract")
print("3, Multiply")
print("4, Divide")

#Assigning the choices
choice = input("\n Enter calculator number{1,2,3,4}: ")
#the calculations
num1 =int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
if choice=="1":
    print(num1," + ",num2," = ",add(num1,num2))
elif choice=="2":
     print(num1," - ",num2," = ",subtract(num1,num2))
elif choice=="3":
     print(num1," * ",num2," = ",multiply(num1,num2)) 
elif choice=="4":
     print(num1," / ",num2," = ",divide(num1,num2)) 
else:
    print("Invalid input")                  

