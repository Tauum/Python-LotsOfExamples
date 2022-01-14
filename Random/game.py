# SETUP
import pygame
import time
import button
#from button import Button
#import button

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Game...')

def drawText(text, x, y, colour, fontFace, size):
    font = pygame.font.Font(fontFace, size)
    textSurface, textRect = getTextObjs(text, font, colour)
    textRect.center = (x, y)
    gameDisplay.blit(textSurface, textRect)

def getTextObjs(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

# THE USER DOES SOMETHING TO START THE GAME.
gameRunning = True
gameTime = 0
anim = False
trainX = 0
trainY = 300
sunX = 600
sunW = 30
#timer += .1
#t = round(timer)
#[btn.x, btn.y, btn.width, btn.height]

#sun = pygame.image.load("/Users/mac/Desktop/ray-clipart-sun-japanese-9.png")

# THE GAME LOOP.
while gameRunning:
    gameTime += 1

    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameRunning = False
            elif event.key == pygame.K_s:
                if anim:
                    anim = False
                else:
                    anim = True

        elif event.type == pygame.MOUSEMOTION:
            print(event.pos)
    mouseX = event.pos[0]
    mouseY = event.pos[1]
   # elif event.type == pygame.MOUSEBUTTONDOWN: ()
   # if mouseX >= btn.X and mouseX <= btn.X + Btn.Width:
    #    if mouseY >= btn.Y and mouseY <= btn.Y + Btn.Height:
    #        print
     #       "test"

    gameDisplay.fill((255, 255, 255))
    pygame.draw.rect(gameDisplay, (0, 0, 255), [trainX, trainY, 200, 50])
    pygame.draw.circle(gameDisplay, (255, 0, 0), [trainX + 20, trainY + 50], 10)
    pygame.draw.circle(gameDisplay, (255, 0, 0), [trainX + 100, trainY + 50], 10)
    pygame.draw.circle(gameDisplay, (255, 0, 0), [trainX + 180, trainY + 50], 10)

    #tempSun = pygame.transform.scale(sun, (int(sunW), int(sunW)))
    #gameDisplay.blit(tempSun, (sunX, 30))

    #drawText("Hello", (200, 500), (100, 100, 100),"Bad Signal.otf", 70)
    #drawText(str(int(gameTime / 100)), (500, 600), (100, 100, 100), "Bad Signal.otf", 40)

    pygame.display.update()

    if anim:
        trainX += 2
        sunX -= 2

# CLEAN UP WHEN FINISHED.
pygame.quit()
quit()