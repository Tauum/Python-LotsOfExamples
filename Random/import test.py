import pygame
import nltk
import time
from button import *
#from button import Button
#import button

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Game...')

GameRunning= True

#variables
timer = 1
mouseX = 0
mouseY = 0
#btn = Button(buttonx, buttony, buttonW, buttonH)
btn = Button(100, 100, 100, 50)

def drawText(text, x, y):
    while GameRunning == (True):
         Start= input('type Y to begin')
    if Start.lower() == 'y':
        GameRunning += 1
    else: print("sorry that was an incorrect input")

while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    for pygame in event.get():
            elif event.type == pygame.KEYDOWN :()
                if event.key == pygame.K_q:
                    gamerunning = False
    elif event.type == pygame.MOUSEMOTION:()
    mouseX = event.pos[0]
    mouseY = event.pos[1]
    elif event.type == pygame.MOUSEBUTTONDOWN:()
    if mouseX >= btn.X and mouseX <= btn.X + Btn.Width:
      if mouseY >=btn.Y and mouseY <=btn.Y + Btn.Height:
          print "test"

gameDisplay.fill ((255, 255, 255))

timer += .1
t = round(timer)
drawText ("(" + str(mouseX) + ", )")


[btn.x, btn.y, btn.width, btn.height]

#btn.

pygame.quit()
quit()