#Author: Emil
#Description: Countdown

import time
from datetime import datetime
from playsound import playsound
  
#function to use our alarm feature
def alarm(alarm_time):
    print("Your alarm will go off at: " + alarm_time)
    
    #need to check if alarm is either am or pm
    if alarm_time[-2] == 'am':
        half = ' am' #half for which half of the day?
    else:
        half = ' pm'

    while True:
        time.sleep(1)
        current_time = datetime.now()
        current = current_time.strftime("%I:%M:%S")
        print(current)
        if current+half == alarm_time: #we'll add the half variable here as current doesn't include am/pm
            playsound("alarm-sound.wav")#plays our installed alarm sound file
            print("Wakey Wakey!")
            break

#make sures our user entered correct format for our alarm
def check_alarmInput(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            print("Invalid HOUR format. Please try again...")
        elif int(alarm_time[3:5]) > 59:
            print("Invalid MINUTE format. Please try again...")
        elif int(alarm_time[6:8]) > 59:
            print("Invalid SECOND format! Please try again...")
        elif alarm_time[-2:] not in ['am', 'pm']:
            print("Invalid AM/PM format! Please try again...")
        else:
            return True

#count down function
def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
      
    print('Times Up!!!!')
    playsound("short-alarm-sound.wav") #plays short alarm sound once countdown is done

#function to reset our program or not
def reset(): 
    reset = input("Do it again? (Y/N)").lower()
    if reset == 'y':
        return True
    else:
        return False

print("Hello to your Alarm and Countdown Program!")

while True:
    option = input("Enter 'A' for Alarm or 'C' for Countdown: ").upper()

    if option == 'A': #if user decides to use alarm
        while True:
            alarm_time = input("Enter alarm time in 'HH:MM:SS AM/PM' format: ")
            acceptable = check_alarmInput(alarm_time.lower())
            if acceptable == True:#will make sure user entered time in correct format
                break
        alarm(alarm_time) #runs our alarm function

    elif option == 'C': #if user decides to use countdown
        while True:
            try:
                t = input("Enter the time in seconds: ")
                countdown(int(t)) #runs our countdown function
                break
            except ValueError: #if user didn't enter a number
                print("Enter an INTEGER please")
    else:
        print("Not a valid input")
    
    start_over = reset()#asks if user wants to restart program
    if start_over == False:#if they don't, then we'll end our program
        print("cya!")
        break


