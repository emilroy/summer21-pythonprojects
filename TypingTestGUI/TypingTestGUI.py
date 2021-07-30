#Author: https://techvidvan.com/tutorials/project-in-python-typing-speed-test/
#Description: Just me, Emil, following the websites tutorial and making comments to understand how to create this typing test GUI

import pygame
from pygame.locals import *
import sys
import time
import random

# 750 x 500    
    
class Game:
   
    def __init__(self):
        self.w=750 #width
        self.h=500 #height
        self.reset=True #to reset the game or not
        self.active = False
        self.input_text='' #text the user will be typing in
        self.word = ''
        self.time_start = 0 #time user started typing
        self.total_time = 0 #total time that the user typed
        self.accuracy = '0%' #how accurately user copied the displayed text
        self.results = 'Time:0 Accuracy:0 % Wpm:0 ' #to display the results
        self.wpm = 0 #words per minute
        self.end = False #ending the game or not
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240) 
        self.RESULT_C = (255,70,70) 
        
       
        pygame.init() #initializing our pygame
        self.open_img = pygame.image.load('type-speed-open.png') #to load our images
        self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h)) #scales our loaded image based on our set width and height


        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500,750))

        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Type Speed test') #name of the window title
       
    #helper function to draw the text in our game window.     
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        text_rect = text.get_rect(center=(self.w/2, y)) #make sure everything is centered
        screen.blit(text, text_rect)
        pygame.display.update() #after drawing anything, pygame requires you to update itself
    
    #gets a random sentence from the sentence.txt file for the user to try typing out
    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n') #splits all sentences by new line
        sentence = random.choice(sentences) #chooses random sentence
        return sentence

    # function to return the results of user typing out the random sentence displayed
    # it'll get the accuracy, WPM, and time user took to type out the sentence
    def show_results(self, screen):
        if(not self.end):
            #Calculate time from when user first clicked in text box and then pressed Enter
            self.total_time = time.time() - self.time_start
               
            #Calculate accuracy
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[i] == c: #counts how many correct characters user inputted based on the random sentence
                        count += 1 
                except: 
                    pass
            self.accuracy = count/len(self.word)*100 #accuracy equation
           
            #Calculate words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)  #WPM equation
            self.end = True
            print(self.total_time)
                
            #the text that'll show the results after user entered their text
            self.results = 'Time:'+str(round(self.total_time)) +" secs   Accuracy:"+ str(round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('icon.png') #loads reset picture
            self.time_img = pygame.transform.scale(self.time_img, (150,150)) #scales reset picture to desired size
            #screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w/2-75,self.h-140))
            self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100)) #displayes the reset picture and button
            
            print(self.results) #displayes all results
            pygame.display.update() #updates pygame as required when making display changes
    
    #main method that'll handle all the events. 
    def run(self):
        self.reset_game() #to make sure to reset all variables
    
       
        self.running=True
        while(self.running):
            clock = pygame.time.Clock() #starts the clock to calculate the time
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT: #when user exits out of program
                    self.running = False
                    sys.exit(0) #FIX-----------before, code giving error with just sys.exit() so added 0 in parameters to resolve that
                elif event.type == pygame.MOUSEBUTTONUP: #if user clicks in the text box, that'll when game will start running
                    x,y = pygame.mouse.get_pos() #makes sure mouse was clicked in text box
                    # position of input box
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time() #user MUST press inside the input box after they reset. if they just start typing otherwise, they total
                                                      #time will be largely incorrect
                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and self.end): #if user clicks the position of reset button, it'll reset game
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN: #when user presses enter to indicate they're done, or a backspace to remove one character
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN: #when user presses enter to indicate they are done
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results) #prints out the results
                            self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            
                        elif event.key == pygame.K_BACKSPACE: #if user presses backpsace, it'll remove one character from the input text box
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode #if the key entered isn't backspace or enter, it'll put it in the box
                            except:
                                pass
            
            pygame.display.update()
             
                
        clock.tick(60)
    
    #function to reset all variables for when game first starts or user wants to start over
    def reset_game(self):
        self.screen.blit(self.open_img, (0,0)) #blit means to draw. so this shows our opening image for a second


        pygame.display.update()
        time.sleep(1)
        
        #resetting all variables
        self.reset=False
        self.end = False

        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence 
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        #drawing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg,80, 80,self.HEAD_C)  
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)

        # draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()


Game().run() #created object of Game class to run our game
