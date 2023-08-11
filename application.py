#dictionary application.
fstudent={'name':'lydia','age':22,'courses':['eng','math']}
mstudent={'name':'leo','age':28,'courses':['eng','math']}
female=fstudent
male=mstudent

print(fstudent['name'])
fstudent['weight']='64'
print(fstudent)
for key,value in fstudent.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print(' ')

if female==fstudent:
    print("Student details are: ", fstudent)
else:
     print("Student details are: " ,mstudent)
