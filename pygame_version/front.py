import pygame as pg
from constants import *

# this class contains all the frontend of the game
class Front:
    def __init__(self) -> None:
        self.board = []
        
    def draw_squares_secrets(self, win):
        win.fill(SKY_BLUE)
        list_of_squares = []

        total_width = NUMBER_OF_SQUARES * SQUARES + (NUMBER_OF_SQUARES - 1) * 10
        start_x = (WIDTH - total_width) // 2
        for i in range (NUMBER_OF_SQUARES+1):
            x = start_x + i * (SQUARES + 10)
            y = (HEIGHT - SQUARES) * 0.8
            list_of_squares.append((x, y, SQUARES, SQUARES))

        for squares in  list_of_squares:
            pg.draw.rect(win, WHITE, squares)
    
    def draw_squares_player(self, win):
        list_of_squares_player = []
        for i in range (4):
            x = (WIDTH - 6 * SQUARES_PLAYER) // 2 + i *  (SQUARES_PLAYER + 10)
            y = (HEIGHT - SQUARES_PLAYER) * 0.5
            list_of_squares_player.append((x, y, SQUARES_PLAYER, SQUARES_PLAYER))

        for squares in  list_of_squares_player:
            pg.draw.rect(win, WHITE, squares)