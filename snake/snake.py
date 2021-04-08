import random
import pygame
import sys
from pygame.locals import *

#基本参数设置
Snake_Speed = 17
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
Green =(0,255.0)
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
    BasicFont=pygame.font.Font('freesansbold.tff',18)
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
    startx =random.randomint(5,Cell_W -6)
    starty =random.randomint(5,Cell_H -6)
    wormCoords =[{'x':startx,'y':starty},
                 {'x':startx-1,'y':starty},
                 {'x':startx-2,'y':starty}]
    direction = setDirection()

    #set the apple's place
    apple = getRandomLocation()

    while True:#main game loop
        for event in pygame.event.get():
            if event.type== QUIT:
                terminate()
            elif event.type==KEYDOWN:
                if (event.key == K_LEFT) and direction !=RIGHT:
                    direction=LEFT
                elif



def showStartScreen():
    ####

def showGameOverScreen():
    ####

def getRandomLocation():
    ###