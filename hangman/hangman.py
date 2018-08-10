import random
import linecache
import os

def askForGuess():
    var = input("Please enter guess letter: ")
    while len(var) > 1:
        var = input("Not a letter, please guess a letter: ")
    return var

def updateWordStatus(status, word, guessed):
    indexes = [i for i, letter in enumerate(word) if letter == guessed]
    for index in indexes:
        status[index] = guessed
    return status
def printHangingMan(curHealth):
    print("|--|")
    if curHealth < 6:
        print("|  O")
        if curHealth == 4:
            print("| \\")
        elif curHealth == 3:
            print("| \|")
        elif curHealth < 3:
            print("| \|/")
    if curHealth == 1:
        print("| /")
    if curHealth == 0:
        print("| / \\")
    for i in range(curHealth - int((curHealth/2))):
            print("|")
    print("__")

cwd = os.getcwd()
wordsFile = cwd +"/words.txt"
health = 6
chosenWordIndex = random.randint(0,1000)
chosenWord = linecache.getline(wordsFile, chosenWordIndex)
guessed = []
wordStatus = []
victory = False
for i in range(len(chosenWord)-1):
    wordStatus.append("-")

while health >0 and not victory:
    print(wordStatus)
    print("Health: " + str(health))
    guess = askForGuess()
    if guess in guessed:
        print("AlreadyGuessed")
    elif guess in chosenWord and guess not in guessed:
        print("Success")
        updateWordStatus(wordStatus,chosenWord,guess)
        if "-" not in wordStatus:
            victory = True
        guessed.append(guess)
    elif guess not in chosenWord and guess not in guessed:
        health = health - 1
        print("incorrect")
        guessed.append(guess)
    printHangingMan(health)
if victory:
    print("You have guessed the word!")
else:
    print("You lose!")
    print("Your word was " + chosenWord)





        
