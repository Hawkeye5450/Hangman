# This is a hangman game

import os.path
import random


class HangmanGame:

    def __init__(self):
        self.guessedWord = []
        self.chosenWord = ""
        self.dictionary = []

    def readDictionary(self, filePath):
        file = open(filePath, 'r')
        self.dictionary = file.read().splitlines()
        print("Added ", len(self.dictionary), "words to the dictionary")
        file.close()

    def chooseWord(self, length = 5):
        temp = self.dictionary.copy()
        self.dictionary.clear()
        for word in temp:
            if len(word) == length:
                self.dictionary.append(word)
        print("There are ", len(self.dictionary), "words of length ", length)
        self.chosenWord = self.dictionary[random.randint(0, len(self.dictionary))]
        self.guessedWord.clear()
        self.guessedWord.extend([False] * length)

    def makeGuess(self, guess):
        for index in range(0, len(self.chosenWord)):
            if self.chosenWord[index] == guess:
                self.guessedWord[index] = True
        return self.guessedWord.count(True)


if not os.path.isfile("dictionary.txt"):
    print("Dictionary file not found. Program ended")
    quit()
else:
    print("Reading dictionary file")
    game = HangmanGame()
    game.readDictionary("dictionary.txt")
    length = int(input("How long of a word do you want? "))
    game.chooseWord(length)
    numCorrect = 0
    lastNumCorrect = 0
    numGuesses = length

    while numCorrect != length and numGuesses != 0:
        numCorrect = game.makeGuess(input(str(numGuesses) + " guesses left\nWhat character do you want? "))

        if numCorrect == lastNumCorrect:
            numGuesses -= 1
        else:
            lastNumCorrect = numCorrect

        for index in range(0, len(game.chosenWord)):
            if game.guessedWord[index]:
                print(game.chosenWord[index], end = '')
            else:
                print('_', end = '')
        print('\n')
    if numCorrect == length:
        print("Congratulations!! The word is ", game.chosenWord)
    else:
        print("Sorry, the word was ", game.chosenWord)
