# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 01:43:40 2018

@author: Anjani K Shiwakoti
"""

import random

# load a text file containing english words
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    letterCount = 0
    for letter in secretWord:
        if (letter in lettersGuessed):
            letterCount += 1
    if (letterCount == len(secretWord)):
        return True
    else:
        return False
    
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    guessedString = []
    rightGuesses = []
    
    for letter in secretWord:
        guessedString.append('_')
        
    for i,letter in enumerate(secretWord):
        if (letter in lettersGuessed):
            guessedString[i] = letter
                
    rightGuesses = " ".join(guessedString)
                
    return (rightGuesses)
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    availableLettersList = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        if letter in availableLettersList:
            availableLettersList.remove(letter)
    return ("".join(availableLettersList))

        
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    global lettersGuessed
    global rightGuesses
    global guessedLetter
    availableLetters = ""
    lettersGuessed = []
    wrongAttempts = 0
    rightGuesses = getGuessedWord(secretWord, lettersGuessed)
    
    print("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is: " + str(len(secretWord)) + " letters long.")

    while True:
        print ("__________________________________________________________")
    
        if (isWordGuessed(secretWord, rightGuesses)):
            print ("Congratulations, you won!")
            break
        elif (wrongAttempts == 8):
            print ("Sorry, you ran out of guesses. The word was", secretWord,".")
            break
        else:
            print ("You have", (8-wrongAttempts), "guesses left.")
         
            availableLetters = getAvailableLetters(lettersGuessed)
        
            print("Available letters: ", availableLetters)  
        
            guessedLetter = input("Please guess a letter: ")
        
            if (guessedLetter in lettersGuessed):
                print ("Oops! You've already guessed that letter: ", end="")
                print(rightGuesses)
            else:
                lettersGuessed.append(guessedLetter)
                rightGuesses = getGuessedWord(secretWord, lettersGuessed)
            
                if (guessedLetter in secretWord) :
                    print ("Good guess: ", end="")        
                    print (rightGuesses)
                else:
                    wrongAttempts += 1
                    print ("Oops! That letter is not in my word: ", end="")
                    print(rightGuesses)

    # end of while loop 

# end of function

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
