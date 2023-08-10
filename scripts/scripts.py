import platform
import getpass

print('You are running a {} machine'.format(platform.system()))
print('Welcome to Python scripting. Please create account to continue.')
print('Your username is:{}'.format(getpass.getuser()))
password_1 = getpass.getpass(prompt='Enter your password:')
password_2 = getpass.getpass(prompt='Re-enter your password:')
if password_1 == password_2:
    print('Successfully logged in')
else:
    print('Unauthorized user')