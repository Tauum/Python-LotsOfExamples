import pygame
import pygame as PG
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Block(PG.sprite.Sprite):
    def __init__ (self, colour, width, height):
        super().__init__()

        self.image = PG.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()

    def ResetPosition(self):
        self.rect.y = random.randint(-300, -20)
        self.rect.x = random.randint(0, WinW)

    def update(self):
        self.rect.y += 1

        if self.rect.y > 410:
            self.ResetPosition()

class Player(Block):
    def Update(self):
        pos = PG.mouse.get_pos()
        self.x.rect = pos[0]
        self.y.rect = pos[1]


PG.init()
WinW = 700
WinH = 400
GameDisplay = PG.display.set_mode((WinW, WinH))

BlockList = PG.sprite.Group()

AllSpritesList = PG.sprite.Group()

for i in range(50):
    Block = Block(BLACK, 10, 10)
    Block.rect.x = random.randint(0, WinW)
    Block.rect.y = random.randint(0, WinH)

    BlockList.add(Block)
    AllSpritesList.add(Block)

Player = Player(BLUE, 20, 20)
AllSpritesList.add(Player)

GameRunning = True
Clock = pygame.time.Clock()
Score = 0

while GameRunning:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            GameRunning = False

    gameDisplay.Fill(WHITE)

    AllspritesList.update()
    BlockHitList = pygame.sprite.spritecollide(Player, BlockList, False)

    for Block in BlockHitList:
        Score += 1
        print(score)
        Block.resetPosition()

    AllSpritesList.draw(gameDisplay)
    clock.tick(60)

    PG.display.flip()

PG.quit()