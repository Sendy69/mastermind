import pygame

### This file contains all the logic part of the game
class Game :
    def __init__(self, win) -> None:
        self._init()
        self.win = win
    
    def update_game(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()