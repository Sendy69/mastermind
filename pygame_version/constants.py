import os
import pygame as pg 
import random

# Size of the game
WIDTH = 1000
HEIGHT = 720

# set of combination
SET_OF_NUMBERS = set(random.randint(1, 10) for _ in range(6))
NUMBER_OF_SQUARES = len(SET_OF_NUMBERS)

# Colors in RGB
RED = (255, 102, 102)
GREEN = (144, 238, 144) 
ORANGE = (255, 178, 102)
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)

# Create a squares secrets combination
SQUARES = 120
# Create a squares player combination
SQUARES_PLAYER = 100




        
