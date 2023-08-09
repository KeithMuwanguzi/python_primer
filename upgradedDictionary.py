import json

#opening the dictionary.json file in read mode
fin = open("dictionary.json","r")#r for reading the file

#reading the contents for json file to cont object
content = json.load(fin)

#function for displaying words with a specific letter
def dispWords():
    letter = (input("Enter a letter to display words with which it begins with ")).lower()
    for i in content:
        if i.startswith(letter):
            print(i)


# to find a word and display if its in the dictionary or not
def findWord():
    word = input("Enter the word to check in the dictionary: ").lower()
    found = False
    for i in content:
        if i == word:
            found = True
    if found == False:
        print("No such word is in the dictionary")
    else:
        print("It is in there in the dictionary!") 


#function to display the meaning
def  dispMeaning():
    word = input("Enter the word to check the meaning: ").lower
    found = False
    for key,value in content.items():
        if key == word:
            found = True
            print("{} word has meeaning {}" .format(key,value))
    if found == False:
        print("No such word exists")


#function to display meaning for the specific word thats there in the meaning of the word. 
def dispSpecificMean():
    word = input("Enter a word to be searched in the dictionary and to display the meaning")
    found = False
    for key,value in content.items():
        if key == word or word in value:
            found = True
            print("Word {} - Meaning {}".format(key,value))#word and meaning will be the curry brackeks
    if found == False:
        print("No such word in the dictionary")


#function for searching words by number of letters
def searchNoofLetters():
    num = int(input("Enter number of letters of length of the word:"))
    found = False
    for key in content:
        if len(key)== num:
            print(key)
            found = True
    if found == False:
        print("No words with this specific length")


while True:
    try:
        print("""
        I N T E R A C T I V E    D I C T I O N A R Y
        ==============================================
        1.Display the words that begin with a specific letter
        2.Find a specific word
        3.Display meaning of the specific word
        4.Display the words-meanings for the specific word that is there
        5.Search and display words by number of their letters
        6.Exit
        """)
        choice = int(input("Enter your choice of operation (1-6): "))
        if choice ==1:
            dispWords()
        elif choice ==2:
            findWord()
        elif choice == 3:
            dispMeaning()
        elif choice == 4:
            dispSpecificMean()
        elif choice == 5:
            searchNoofLetters()
        elif choice == 6:
            break
        else:
            print("Invalid number!! Enter any number between 1-6")
    except:
        print("Invalid input")





      
