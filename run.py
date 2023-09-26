import sys
import os
import pygame

import .codeNAssets/generateGame
from .codeNAssets import player

def getMiniMap(map,X,Y):
    """
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 P 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    """
    #screen dimensions are 17 width, 9 height in blocks
    #note that as X increases, it moves to the right, as y increases, it moves down
    MiniMapX = X - 8 #top left corner
    MiniMapY = Y - 4 

    miniMap = [[map[i][j] for i in range(MiniMapX,MiniMapX+17)] for j in range(MiniMapY,MiniMapY+9)]

    return miniMap

#def showScreen(miniMap):

def main():

    screen = open('screen.txt','w')
    seed = int(input('yeah insert seed')) #proto
    name = int(input('yeah insert name')) #proto
    map = generateGame.generateMap(seed,name)
    print('generating map')
    
    while True:
        Y = int(input('Y: '))
        X = int(input('X: '))
        miniMap = getMiniMap(map,X,Y)
        for i in range(17):
            for j in range(9):
                screen.write(str(miniMap[i][j])+' ')
        screen.write('\n')