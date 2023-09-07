answer = input("What is the answer to the Greatest question of life, the Universe and Everything?").lower()
match answer:
    case '42'|'forty-two'|'forty two':
        print('Yes')
    case _:
        print('No')