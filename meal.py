def main(time):
    new_time = convert_time(time)
    if new_time >= 7 and new_time <= 8:
        print('Breakfast time')
    elif new_time >= 12 and new_time <= 13:
        print('Lunch time')
    elif new_time >= 18 and new_time <= 19:
        print('Dinner time')


def convert_time(time):
    if time.__contains__(':'):
        hours,minutes = time.split(':')
        hours = int(hours)
        if int(minutes) > 59:
            print('Invalid Time')
        else:
            minutes = int(minutes)/60
            new_time = hours + minutes 
            return new_time
    else:
        print('Invalid Time Format')
        return 00.00


if __name__ == '__main__':
    time = input('What is the time?:')
    main(time)



