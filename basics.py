import constants

#Basic Syntax
print('Let\'s get this started')

#Variables and data types
num = 1
name = 'Keith Muwanguzi'
# print(name)

a,b,c = 1,2,"Home"
some_binary = 0b001
result = True
# print(c)

x = y = 'Data Unloaded'
z = x
# print(x,y,z)

# print(constants.PI)
# print(some_binary)

value = 0b011
print(value,'is of the type:',type(value))

print('Good Morning', end=' ')
print('I hope you are kawa')
print('New Year',2020,'Is here',sep='-')
x = 1
y = "the value is:"
z =input('Enter the value:')

print('For the developed code, {}{}. For all the others, the value is: {}'.format(y,x,z))