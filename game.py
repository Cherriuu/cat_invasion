import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    pygame.init() # creates the blank slate and initiates needed settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # sets the screen size, this is called a surface
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    bg_color = (0,0,255) # pygame background colors range from 0 to 255 and uses red, green, and blue mixes

    while True: # surface is redrawn through every iteration of this
        # this is called an event loop that will perform a task based off the kind of event that has occured

        # the event loop detects any keyboard or mouse movements and runs if it detects them
        gf.check_event()

        gf.update_screen(ai_settings, screen, ship)


run_game()