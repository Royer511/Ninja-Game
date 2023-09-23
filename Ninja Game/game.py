import pygame
import sys

pygame.init()

# sets up are game screen
screen = pygame.display.set_mode((640,480))

# set_caption changes the name in the window
pygame.display.set_caption("Ninja Game")

#forces game to run at 60 fps - good to set it for stability
clock = pygame.time.Clock()

# each game are frames in iteration inside a loop, every loop you need to update everything, than you put it on the screen, than you update the screen. games are continuous loops. 
while True:
    # need input, if no input, windows will think your not taking input and windows will think the app has stopped responding.
    for event in pygame.event.get(): # this function will get that input --  event could be anything: mouse touch, keystroke ect
        if event.type == pygame.QUIT: # you actually need to code the 'x' on the top right lol
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)