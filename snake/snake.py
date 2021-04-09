import random
import pygame
import sys
from pygame.locals import *

#基本参数设置
Snake_Speed = 10
Window_Width = 800
Window_Height =500
Cell_Size = 20

#获取宽高格数
assert Window_Width % Cell_Size ==0,"window width must be a multiple of cell size"
assert Window_Height % Cell_Size ==0,"window height must be a mutliple of cell size"
Cell_W= int(Window_Width/Cell_Size)
Cell_H= int(Window_Height/Cell_Size)

#color setting
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green =(0,255,0)
DarkGreen=(0,155,0)
DarkGray=(40,40,40)
Yellow=(255,255,0)
DarkRed=(150,0,0)
Blue = (0,0,255)
DarkBlue=(0,0,150)

Bgc = Black
UP='up'
DOWN='down'
LEFT='left'
RIGHT='right'

HEAD=0 #index of snake's head

def main():
    global SnackeSpeedClock,DisplaySurf,BasicFont

    pygame.init()
    SnackeSpeedClock=pygame.time.Clock()
    DisplaySurf=pygame.display.set_mode((Window_Width,Window_Height))
    BasicFont=pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('MySnake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def setDirection():
    rand = random.randint(0, 3)
    if rand == 0:
        direction = UP
    elif rand == 1:
        direction = DOWN
    elif rand == 2:
        direction = LEFT
    else:
        direction = RIGHT
    return direction

def runGame():
    #set a random start point
    startx =random.randint(5,Cell_W -6)
    starty =random.randint(5,Cell_H -6)
    wormCoords =[{'x':startx,'y':starty},
                 {'x':startx-1,'y':starty},
                 {'x':startx-2,'y':starty}]
    direction = setDirection()

    #set the apple's place
    apple = getRandomLocation()

    while True:#main game loop
        #push the key event
        for event in pygame.event.get():
            if event.type== QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if (event.key == K_LEFT) and direction !=RIGHT:
                    direction=LEFT
                elif(event.key == K_DOWN) and direction !=UP:
                    direction=DOWN
                elif(event.key == K_UP) and direction != DOWN:
                    direction=UP
                elif (event.key==K_RIGHT) and direction !=LEFT:
                    direction=RIGHT
                elif event.key == K_ESCAPE:
                    terminate()
        #check if the snake has hit itself or the edge
        if wormCoords[HEAD]['x']==-1 or wormCoords[HEAD]['x']==Cell_W or wormCoords[HEAD]['y']==-1 or wormCoords[HEAD]['y']==Cell_H:
            return #game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y']==wormCoords[HEAD]['y']:
                return #gameover


        #check the snake eat the apple
        if wormCoords[HEAD]['x']==apple['x'] and wormCoords[HEAD]['y']==apple['y']:
            #dont remove the tail segment
            apple =getRandomLocation()
        else:
            del wormCoords[-1]
            #remove snakes' tail

        #move the worm by adding a new segment in the direction it is moving
        if direction == UP:
            newHead = {'x':wormCoords[HEAD]['x'],
                       'y':wormCoords[HEAD]['y']-1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}

        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x']-1,
                       'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x']+1,
                       'y': wormCoords[HEAD]['y']}

        wormCoords.insert(0,newHead)
        DisplaySurf.fill(Bgc)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords)-3)
        pygame.display.update()
        SnackeSpeedClock.tick(Snake_Speed)

def drawPressKeyMsg():
    pressKeySurf = BasicFont.render('Press a key to start',True,White)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (Window_Width - 200,Window_Height-30)
    DisplaySurf.blit(pressKeySurf,pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT))>0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents)==0:
        return None
    if keyUpEvents[0].key== K_ESCAPE:
        terminate()
    return keyUpEvents[0].key



def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf',100)
    titleSurf1=titleFont.render('Snake!',True,White,DarkGreen)
    degrees1 = 0
    degrees2 = 0
    while True:
        DisplaySurf.fill(Bgc)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1,degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (Window_Width/2,Window_Height/2)
        DisplaySurf.blit(rotatedSurf1,rotatedRect1)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()#clear event queue
            return
        pygame.display.update()
        SnackeSpeedClock.tick(Snake_Speed)
        degrees1 +=3 #rotate by 3 degrees each frame
        degrees2 +=7 #rotate by 7 degrees each frame


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf',100)
    gameSurf = gameOverFont.render('Game',True,White)
    overSurf = gameOverFont.render('Over',True,White)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Window_Width/2,10)
    overRect.midtop = (Window_Width/2,gameRect.height+10+25)

    DisplaySurf.blit(gameSurf,gameRect)
    DisplaySurf.blit(overSurf,overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()#clear out any key press in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()#clear event queue
            return

def getRandomLocation():
    return {'x':random.randint(0,Cell_W-1),'y':random.randint(0,Cell_H-1)}

def terminate():
    pygame.quit()
    sys.exit()

def drawGrid():
    for x in range(0,Window_Width,Cell_Size):
        pygame.draw.line(DisplaySurf,DarkGray,(x,0),(x,Window_Height))
    for y in range(0,Window_Height,Cell_Size):
        pygame.draw.line(DisplaySurf,DarkGray,(0,y),(Window_Width,y))

def drawWorm(worm):
    for coord in worm:
        x=coord['x']*Cell_Size
        y=coord['y']*Cell_Size
        wormSegmentRect = pygame.Rect(x,y,Cell_Size,Cell_Size)
        pygame.draw.rect(DisplaySurf,DarkGreen,wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x+4,y+4,Cell_Size-8,Cell_Size-8)
        pygame.draw.rect(DisplaySurf,Green,wormInnerSegmentRect)

def drawApple(coord):
    x= coord['x']*Cell_Size
    y=coord['y']*Cell_Size
    appleRect = pygame.Rect(x,y,Cell_Size,Cell_Size)
    pygame.draw.rect(DisplaySurf,Red,appleRect)

def drawScore(score):
    scoreSurf = BasicFont.render('Score:%s' %(score),True,White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Window_Width -120,10)
    DisplaySurf.blit(scoreSurf,scoreRect)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
