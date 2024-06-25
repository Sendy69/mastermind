##### Partie FrontEnd avec Pygame 
import sys
import os
import pygame
from game import Game
from constants import *
from front import *

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import the required functions






FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Mastermind')

def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    front = Front()
    

    while run:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        # RENDER YOUR GAME HERE
        front.draw_squares_secrets(WINDOW)
        front.draw_squares_player(WINDOW)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
 

if __name__ == "__main__":
    main() 
