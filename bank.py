greeting = input('Greeting:').lower()
greet_arr = greeting.split(' ')
match greet_arr[0]:
    case 'hello':
        print('$0')
    case _:
        if greeting[0] == 'h':
            print('$20')
        else:
            print('$100')