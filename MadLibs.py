#Author: Emil Roy
#Description: Creates story based off of user inputs

name = input("Welcome to a Mad Libs Generator! What's your name?")
print("Hey ", name, "! Let's get started")

while True:
    story = input("""Which story do you want to create? \n 
    1) Roses are...\n
    2) Twinkle Twinkle\n
    3) Hickory Dickory Dock\n
    Enter 1, 2, or 3: """)

    if story == '1':
        pluralNoun = input("Enter a plural noun: ")
        redThing = input("Something red: ")
        size = input("Small, Medium, or Large?: ")

        print("=========Your Mad Libs Story=========")
        print(pluralNoun + " are red")
        print(redThing + " is too")
        print("I ordered a " + size + ", and none of it is for you.")

        reset = input("Do you want to create another story? (Y/N)").lower()
        if reset == 'y':
            continue
        else:
            print("See you later!")
            break

    elif story == '2':
        firstNoun = input("Enter a noun: ")
        place = input("Enter a place: ")
        secondNoun = input("Enter another noun: ")

        print("=========Your Mad Libs Story=========")
        print("Twinkle, twinkle, little " + firstNoun + ',')
        print("How I wonder what you are!")
        print("Up above the " + place + " so high,")
        print("Like a " + secondNoun + " in the sky.")
        print("Twinkle, twinkle, little " + firstNoun + ',')
        print("How I wonder what you are!")

        reset = input("Do you want to create another story? (Y/N)").lower()
        if reset == 'y':
            continue
        else:
            print("See you later!")
            break

    elif story == '3':
        hickorySubject = input("Enter a noun: ")
        furniture = input("Enter a furniture: ")
        number = input("Enter a number: ")

        print("=========Your Mad Libs Story=========")
        print("Hickory, dickory, dock.")
        print("The " + hickorySubject + " ran up the " + furniture + '.')
        print("The " + furniture + " struck " + number + ',')
        print("The " + hickorySubject + " ran down,")
        print("Hickory, dickory, dock.")

        reset = input("Do you want to create another story? (Y/N)").lower()
        if reset == 'y':
            continue
        else:
            print("See you later!")
            break
    else: 
        print("Not a valid choice.")
        






