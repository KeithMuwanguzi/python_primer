exp = input('Expression:')
x,y,z = exp.split(' ')
match y:
    case '+':
        print(int(x) + int(z))
    case '*':
        print(int(x) * int(z))
    case '-':
        print(int(x) - int(z))
    case '/':
        if int(z) == 0:
            print('Can not divide by 0')
        else:
            print(int(x) / int(z))