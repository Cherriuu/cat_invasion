import pygame
import game_functions as gf
from pygame.sprite import Group

from settings import Settings
from cat import Cat

from mouse import Mouse
from game_stats import GameStats
from button import Button

from scoreboard import Scoreboard

def run_game():
    pygame.init() # creates the blank slate and initiates needed settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # sets the screen size, this is called a surface
    pygame.display.set_caption("Cat Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    cat = Cat(screen, ai_settings)
    bullets = Group()
    mouses = Group()

    gf.create_fleet(ai_settings, screen, cat, mouses)
    print(len(mouses))

    while True: # surface is redrawn through every iteration of this
        # this is called an event loop that will perform a task based off the kind of event that has occured

        gf.check_event(cat, ai_settings, screen, bullets, stats, play_button, mouses, sb)

        if (stats.game_active):

            cat.update()

            gf.update_bullets(mouses, bullets, ai_settings, screen, cat, stats, sb)

            gf.update_mouses(ai_settings, stats, screen, mouses, cat, bullets, sb)

        gf.update_screen(ai_settings, screen, cat, mouses, bullets, stats, play_button, sb)


run_game()