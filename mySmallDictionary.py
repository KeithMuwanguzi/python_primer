# The words are hard coded...just wanted to see if i can apply what i learnt...
#Instructions.....type in "pinl" first...then follow the output.


print("Welcome to My_Dictionary")
dictionary = {'pink':'a light shade of red','pin':'piece of jewellery','pinch':'squeeze tightly between fingers','pinl':'Not found! Try one of these:[pink, pin, pinch]'}
i = 0
while i < 4:
    word = str(input("Enter a word: "))
    i = i + 1
    found = False
    for a in dictionary:
        if a == word:
            found = True
    if found == False:
        print("No such word in the dictionary")
    else:
        print(dictionary[word])
print("Thank you")