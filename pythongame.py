#!/usr/bin/python

import pygame   #for game creation
import random   #for random events in game
import sys      #to exit the game upon gameover

pygame.init() #start pygame

gameop = True #for while loop

black = (   0,   0,   0)
white = ( 255, 255, 255)
red = ( 255,   0,   0)
green = (   0,   255,   0)      #colours
blue = (   0,   0,   255)
green2 = (   56, 128,   36)
yellow = (   245,   245,   100)
window = pygame.display.set_mode((800, 600))  #game window size
pygame.display.set_caption('Python python')     #game title
clock = pygame.time.Clock()     #tracks the time
xaxis = [390]   #list for the snake position - starting position is the centre of the screen
yaxis = [290]
width = 19
height = 19             #dimensions of player
Keys = [False, False, False, False]     #for movement direction
Alive = True            #to check for gameover
sprinklelocationx = random.randrange(15, 785)   
sprinklelocationy = random.randrange(15, 585)
score = 0       #scoring
text = pygame.font.SysFont("Arial", 15)         #set game font
text2 = pygame.font.SysFont("Arial", 10)
pause = False

while gameop is True: 
  window.fill(black)        #sets screen to black
  Snakesegment = []     #empty list for the snake body, emptied and refilled for every iteration in the event
  for n in range(len(xaxis) -1, 0, -1):         #this loop draws the snakebody in the position the head/last segment was the previous iteration
    xaxis[n] = xaxis[n-1]                       
    yaxis[n] = yaxis[n-1]       #puts the x and y coords of each segment to those of the previous
    Snakesegment.append(pygame.draw.rect(window, green2, [xaxis[n], yaxis[n], width, height]))  #draws the list and appends the segment to the body list 
  player = pygame.draw.rect(window, green, [xaxis[0], yaxis[0], width, height])         #the player (snake's head)
  sprinkle = pygame.draw.rect(window, yellow, [sprinklelocationx, sprinklelocationy, 9, 9])     #spawns the snake food in the game at random location
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:            #checks for key press
      if event.key == pygame.K_p:
        pause = True            #if P pressed = sets pause as True
        while pause is True:            #while loop keeps game paused until P pressed again
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
              if event.key == pygame.K_p:
                pause = False                   #sets pause as False to break while loop
      if event.key == pygame.K_UP and Keys[1] is not True:      #and statement prevents player from reversing direction
        Keys = [False, False, False, False] 
        Keys[0] = True
      elif event.key == pygame.K_DOWN and Keys[0] is not True:
        Keys = [False, False, False, False]     #resets key list on new key press, then sets that direction as "True"
        Keys[1] = True
      elif event.key == pygame.K_RIGHT and Keys[3] is not True:
        Keys = [False, False, False, False] 
        Keys[2] = True    
      elif event.key == pygame.K_LEFT and Keys[2] is not True:
        Keys = [False, False, False, False] 
        Keys[3] = True
      elif event.key == pygame.K_ESCAPE:        #allows the player to exit the game using escape
        print "Quitting...."
        print "score = ", score
        sys.exit()  

  if Keys[0] is True:
    yaxis[0] -= 10
  elif Keys[1] is True:
    yaxis[0] += 10
  elif Keys[2] is True:         #updates the playerhead position in the direction that was last pressed (True)
    xaxis[0] += 10                       #continues until another button is pressed
  elif Keys[3] is True:
    xaxis[0] -= 10

  if xaxis[0] >= 800 or xaxis[0] <= 0:                  #checks for player collision with the walls of the game
    Alive = False               
  if yaxis[0] >= 600 or yaxis[0] <= 0:
    Alive = False
 
  if Alive is False:                    #If player is "dead" then the game is exited and score is printed to terminal
    Keys = [False, False, False, False] 
    print "GAME OVER"
    print "score = ", score
    sys.exit()

  if player.colliderect(sprinkle):              #checks for collision of player with snakefood
    score += 5                                                 #increase score
    sprinklelocationx = random.randrange(30, 770)       #spawn new food at random location
    sprinklelocationy = random.randrange(30, 570)
    xaxis.append(xaxis[-1])             #copies the last coordinates as a new entry in the list
    yaxis.append(yaxis[-1])
  
  
  for i in range(0, len(Snakesegment) -8):      #the snake tail is stored in the list in reverse order, so collision should ignore the last few entries. 4 is sufficient to not die when moving in a straight line, but collision may happen when turning unless number is increased
    if player.colliderect(Snakesegment[i]):             #if the snake hits its own body
       Alive = False
  
  scoreboard = text.render("Score: " + str(score), 1, white)   #creates a scoreboard object
  instructions1 = text2.render("P = Pause", 1, white)
  instructions2 = text2.render("ESC = Quit", 1, white)
  window.blit(scoreboard, (10, 15))     #creates the scoreboard object in the game window
  window.blit(instructions1, (10, 30)) 
  window.blit(instructions2, (10, 40))
  pygame.event.pump()           #makes the game move through events 
  pygame.display.flip()                 #updates the game window
  clock.tick(60)        #sets the FPS

'''
Difficulty can be adjusted by changing the x and y axis increments and the FPS

Issues:

- turning too fast can cause the snakehead to collide with its body (Resolved?)
- the game window is somewhat misleading in terms of the board edge 
'''