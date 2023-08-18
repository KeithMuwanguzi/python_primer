#classes basics
#creating the class for employees
class Employee:
    num_of_employee = 0
    raise_amount = 1.8
    def __init__(self, first,last,pay):
        self.fname = first
        self.lname= last
        self.pay=pay
        self.email= first+last + '@gmail.com'
        Employee.num_of_employee +=1

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname) 
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)       

emp1 =Employee('lydia','esther', 70000) 
emp2 =Employee("joy","ellen", 80000)  
emp3 =Employee("mike","kennedy", 90000)         

print(emp1.email)
print(emp2.email)
#print(emp3.email)
print(emp1.fullname())
print(emp2.fullname())
print(Employee.num_of_employee)
#printing out the employee raise.
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
emp1.raise_amount = 0.2
# dictonaries in classes
print(emp1.__dict__)
