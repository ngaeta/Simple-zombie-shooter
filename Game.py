# test1_pyganim.py - A very very very basic pyganim test program.
#
# This program just runs a single animation. It shows you what you need to do to use Pyganim. Basically:
#   1) Import the pyganim module
#   2) Create a pyganim.PygAnimation object, passing the constructor a list of image filenames and durations.
#   3) Call the play() method.
#   4) Call the blit() method.
#
# The animation images come from POW Studios, and are available under an Attribution-only license.
# Check them out, they're really nice.
# http://powstudios.com/

import os
import sys

import pygame
from pygame.locals import *
from EnemyManager import EnemyManager
from Player import Player

print(os.getcwd())
pygame.init()

# set up the window
WIDTH = 1280
HEIGHT = 720

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('ZombieShooter')

listCollider = list()
player = Player(pygame.Vector2(0, 360))
EnemyManager.init()

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
fps = 30
background = pygame.image.load('C:\\Users\\ddd\\Desktop\\Workspace Pyton\\AIV\\Assets\\bg2.png')

while True:
    deltaTime = mainClock.tick(fps)
    second = 1 / float(deltaTime)

    #input code
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        player.input(event)
    
    #update code
    player.update()
    EnemyManager.update()

    #draw code
    windowSurface.blit(background, (0, 0))
    player.draw()
    EnemyManager.draw()

    pygame.display.update()