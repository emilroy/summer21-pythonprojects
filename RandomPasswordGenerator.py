#Author: Emil Roy
#Description: creates a random password for you consisting of numbers, letters, and symbols.
#             Also stores those created passwords into a text document for you and keeps track of sites you already added

import random
import string
from os import path #used to check if our pickle file exists or not
import pickle #used to make our sites_list persistent

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation

    #creates random password with random length of 8-12 characters. 
    password = ''.join(random.choice(characters) for i in range(random.randint(10, 15)))

    print("Your random password is: ", password)
    return password

print("Welcome to your password generator where we'll store your passwords in a text document for you")
print("Make sure to enter q when you wish to quit and save\n")

sites_list = []
saved_sites = 'sites.pkl' #file name of where we'll save the names of the site user already added

if path.exists(saved_sites) == false: #if the pickle file doesn't exist yet, it'll create it here
    open_file = open(saved_sites, "wb")
    pickle.dump(sites_list, open_file) #it'll create a pickle file that'll save our added_sites list data
else: 
    open_file = open(saved_sites, "rb")
    sites_list = pickle.load(open_file) #if the pickle file already existed, we will load the saved added_sites list

file = open("passwords.txt", 'a') #opens our password.txt file to append to

while True: 
    print()
    site = input("Which site do you want to create a password for?")
    if site == 'q':
        print("Stay safe!")
        break
    elif site.lower() in sites_list: #to check if user already added the site or not
        print("\nYou already added that site")
    else:
        sites_list.append(site.lower()) #if it's a new site, it'll store that site into our added_sites list

        list = site + '          ' + generate_password() + '\n'
        file.write('\n') 
        file.write(list) #add the site and randomly created password to our .txt document
      
        print("\nSuccessfully added new password!")

open_file = open(saved_sites, "wb")
pickle.dump(sites_list, open_file)#will store the new sites into our pickle file
open_file.close() #closes pickle file

file.close() #closes password file

