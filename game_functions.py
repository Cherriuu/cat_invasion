import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    ship.blitme()
            
    pygame.display.flip() # updates the screen to the latest