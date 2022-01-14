import pygame
import sys
import time
import random


class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50][80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self, dir):
        if dir == "RIGHT" and not of (self.direction) == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not of (self.direction) == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not of (self.direction) == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not of (self.direction) == "UP":
            self.direction = "DOWN"

    def move(self, FoodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UPT":
            self.position[1] += 10
        if self.direction == "DOWN":
            self.position[1] -= 10
        self.body.insert(0, (list(self.position))
        if self.position == FoodPos:
            return 1
        else self.body.pop()
            return 0


def CheckCollision(self):
    if self.position[0] > 490 or self.position[0] < 0:
        return 1
    elif self.position {1} > 490 or self.position[1] < 0:
    return 1
    for bodyPart in self.body[1:]:
        if self.position == bodyPart:
            return 1


return 0


def GetHeadPos(self):
    return self.position


def GetBody(self):
    return self.body


class FoodSpawn():
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.IsFoodOnScreen = True

    def SpawnFood(self):
        if self.IsFoodOnScreen == False:
            self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.IsFoodOnScreen = True
        return self.position

    def SetFoodOnScreen(self, b):
        Self.IsFoodOnScreen = b


window = pygame.display.set_mode(500, 500)
pygame.display.set_caption("TS Snake Game")
fps = pygame.time.Clock()

score = 0

Snake = Snake()
FoodSpawner = FoodSpawner()


def GameOver():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver():
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.ChangeDirTo("RIGHT")
            if event.key == pygame.K_LEFT:
                snake.ChangeDirTo("LEFT")
            if event.key == pygame.K_UP:
                snake.ChangeDirTo("UP")
            if event.key == pygame.K_DOWN:
                snake.ChangeDirTo("DOWN")

FoodPos = FoodSpawner.SpawnFood()
if (Snake.move(FoodPos) == 1):
    score += 1
    FoodSpawner.SetFoodOnScreen(False)

window.fill(pygame.Colour(225, 225, 225))
for pos in Snake.GetBody():
    pygame.draw.rect(window, pygame.Colour(0, 225, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, pygame.Colour(225, 0, 0), pygame.Rect(FoodPos[0], FoodPos[1], (pos[0], pos[1], 10, 10))
    if (Snake.CheckCollision() == 1):
        GameOver()
    pygame.display.set_caption("TS Snake Game Score : " + str(Score))
    pygame.display.flip()
    fps.tick(24)

