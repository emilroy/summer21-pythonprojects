#Author: Emil Roy
#Description: Rock, Paper, Scissors game against the computer

import random

choices = ["rock", "paper", "scissors", 'q'] #available choices
user_wins=0 #number of times the user won
comp_wins=0 #number of times computer won

print("Welcome to Rock, Paper, Scissors! Can you beat the computer?")
print('Enter "q" to quit')
while True:
    rand = random.randint(0,2)
    comp_choice = choices[rand] # to choose random choice in the choices list
    user_choice = input("Rock, Paper, Scissors?").lower()
    while user_choice not in choices: #if user enters a non valid input
        user_choice = input("That's not a valid input. Try again: ").lower()
    
    if user_choice == 'q': #when user wants to quit
        print("Bye now!")
        break

    print()
    print("You chose " + user_choice)
    print("The computer chose "+comp_choice + '\n') 

    if user_choice == comp_choice:
        print("== It's a Tie! ==")
    elif user_choice == 'rock': #when user enters ROCK
        if comp_choice == 'scissors':
            print("== You win! ==")
            user_wins+=1
        else:
            print("== You lose :( ==")
            comp_wins+=1
    elif user_choice == 'paper': #when user enters PAPER
        if comp_choice == 'rock':
            print("== You win! ==")
            user_wins+=1
        else:
            print("== You lose :( ==")
            comp_wins+=1
    elif user_choice == 'scissors': #when user enters SCISSORS
        if comp_choice == 'paper':
            print("== You win! ==")
            user_wins+=1
        else:
            print("== You lose :( ==")
            comp_wins+=1

    print("\nThe score is:\nYou: {} \nComputer: {}\n".format(user_wins, comp_wins))

    print('==================================') #divider between rounds















