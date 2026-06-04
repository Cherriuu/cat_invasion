import sys
import pygame
from bullet import Bullet

def check_event(cat, ai_settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # for every action the user takes (clicking the right arrow, hitting space, etc..)
            sys.exit() # system call to exit the game
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cat, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cat)

def check_keydown_events(event, cat, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        cat.moving_right = True
    elif event.key == pygame.K_LEFT:
        cat.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, cat)
        bullets.add(new_bullet)

def check_keyup_events(event, cat):
    if event.key == pygame.K_RIGHT:
        cat.moving_right = False
    elif event.key == pygame.K_LEFT:
        cat.moving_left = False

def update_screen(ai_settings, screen, cat, bullets):
    screen.fill(ai_settings.bg_color) # redraw the screen during each iteration
    cat.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip() # updates the screen to the latest