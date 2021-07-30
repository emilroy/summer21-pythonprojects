#Author: Emil
#Description: Hangman game

import random
import time

animals = ['tiger', 'peacock', 'elephant', 'iguana', 'dolphin', 'eagle', 'gorilla', 
           'chimpanzee', 'orangutan', 'lobster', 'rabbit', 'lizard', 'parrot', 'walrus']
superheroes = ['deadpool', 'spiderman', 'thor', 'flash', 'hawkeye', 'robin', 'storm'
               'mystique', 'vision', 'aquaman', '', 'ironman', 'daredevil', 'wolverine']
sports = ['basketball', 'football', 'badminton', 'tennis', 'soccer', 'volleyball', 'baseball'
          'cricket', 'hockey', 'golf', 'track','rugby', 'boxing', 'archery', 'bowling']

def getRandomWord(): #function to create randomly generated word from category user chooses
    secretWord = ''

    print("Welcome to Hangman!")
    time.sleep(1)
    print("Enter the number of the category you want to guess from: ")
    print("1)Animals\n2)Super Heroes\n3)Sports")
    choice = input("Your choice is: ")
    while choice not in ['1', '2','3']:
        choice = input("Please only select 1, 2, or 3: ")

    if choice == '1':
        secretWord = random.choice(animals)
    elif choice == '2':
        secretWord = random.choice(superheroes)
    else:
        secretWord = random.choice(sports)
    return secretWord

def displayBoard(attempts): #to display each hangman stage 
    stages = ["""
    H A N G M A N

       +---+
       |   |
           |
           |
           |
           |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
          |
          |
          |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""", """
    H A N G M A N

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========="""]

    time.sleep(1) #to wait 1 second before proceeding
    print(stages[6-attempts]) #because list was backwards lol. could reverse list or just do 6-attempts
    print()

#function to actually start and play the game
def start(secretWord): 
    blanks = '_' * len(secretWord)
    successful = False #to keep track of if they guessed the secret word or not
    userGuesses = [] #to keep track of what letters user already guessed
    attempts = 6 #number of tries the user gets
    guess = ''

    displayBoard(attempts)
    print(blanks)

    while not successful and attempts > 0:
        guess = input("\nEnter a letter: ").lower() #gets the user's guess and makes sure it's a single letter
        if len(guess) != 1:
            print("Please enter only a single letter")
        elif guess in userGuesses:
            print("You already guessed that letter. Try another")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter")
        else: #if user correctly enters only one letter they haven't guessed
            userGuesses.append(guess)
            if guess not in secretWord: #if user doesn't guess a letter that's in the secret word
                print(guess + " is not in the word.")
                attempts-=1
            else:
                print("Great! The letter " + guess + " is in the word!")
                word_as_list = list(blanks) #converts everything in blanks as a list into a new variable
                indices = [i for i, letter in enumerate(secretWord) if letter == guess]#finds indices where the guess is in secret word
                for index in indices: #to replace the blanks with the correctly guessed letters
                    word_as_list[index] = guess
                blanks = "".join(word_as_list)#to join back the replaced blanks with correctly guessed letters
                if "_" not in blanks: #if there are no more blanks, that means user guessed all letters
                    successful = True
            time.sleep(1)
            displayBoard(attempts)
            print(blanks)
 
    if successful: 
       print("======You got it!======")
    else: 
       print("You ran out of tries :( You'll get em next time!")
       print("The secret word was: " + secretWord)

def main(): #to get secret word and start the game
    secretWord = getRandomWord()
    start(secretWord)
    while input("Do you want to try again? (Y/N)").lower() == 'y': #if user wants to repeat the game
        secretWord = getRandomWord()
        start(secretWord)

if __name__ == '__main__': #to run our main function
    main()








