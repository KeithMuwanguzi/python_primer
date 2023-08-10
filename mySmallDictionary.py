
#opening another python file in this one.(sportsDictionary.py)
with open("sportsDictionary.py") as f:
    exec(f.read())


#function for displaying words with a specific letter
def dispWords():
    letter = (input("Enter a letter to display words with which it begins with ")).lower()
    for i in dictionary:
        if i.startswith(letter):
            print(i)


# to find a word and display if its in the dictionary or not
def findWord():
    word = str(input("Enter a word to check if it exists in the dictionary: ")).lower()
    found = False
    for i in dictionary:
        if i == word:
            found = True
    if found == False:
        print("No such word is in the dictionary")
    else:
        print("It exists in the dictionary!") 

#function to display the meaning
def dispMeaning():
    word = input("Enter the word to check the meaning: ").lower()
    found = False
    for key,value in dictionary.items():
        if key == word:
            found = True
            print("{} MEANS {}" .format(key,value))
    if found == False:
        print("No such word exists")


#function for searching words by number of letters
def searchNoofLetters():
    num = int(input("Enter number of letters comprised of the word:"))
    found = False
    for key in dictionary:
        if len(key)== num:
            print(key)
            found = True
    if found == False:
        print("No words with this specific length")

while True:
    try:
        print(""" B A S K E T B A L L   D I C T I O N A R Y
        ===================================================
        1.Display the words that begin with a specific letter
        2.Find a specific word
        3.Display meaning of the specific word
        4.Search and display words by number of their letters
        5.Exit""")

        choice = int(input("Enter your choice of operation (1-5): "))
        if choice ==1:
            dispWords()
        elif choice ==2:
            findWord()
        elif choice == 3:
            dispMeaning()
        elif choice == 4:
            searchNoofLetters()
        elif choice == 5:
            break
        else:
            print("Invalid number!! Enter any number between 1-5")
    except:
        print("Invalid input")





#opening the dictionary.json file in read mode
#....fin = open("dictionary.json","r")#r for reading the file

#reading the contents for json file to cont object
#......content = json.load(fin)

