#Author: Emil
#Description: Guess the random number the computer generated

import random

while True: 
    print("Guess the number from 1-100, you have 7 tries!")
    tries=1 # number of attempts user tried
    guess=0 # the guess user tried
    number = random.randint(1,100) # creates the randomly generated number

    while tries < 7: #after 7 tries, user lost the game
        guess=int(input("Try " + str(tries) + ": "))
        tries+=1
        if guess < number:
            print("Too low!")
        elif guess > number: 
            print("Too high!")
        else:
            break
    if guess == number: #if user successfully guesses the number
        print("You got it! Only took you " + str(tries-1) +" tries!")
    else:
        print("Shucks, you didn't get it, the number was "+ str(number))

    reset = input("Do you want to try again? (Y/N)").lower() #to ask user if they want to repeat the game
    if reset == 'y':
        print("==================") # to distinguish between rounds
        continue
    else: # anything else other than a 'y' is going to end the game
        print("Bye-Bye!")
        break



