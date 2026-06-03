import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp') # load the image in and save it to self.image
        self.rect = self.image.get_rect() # .get_rect wraps the image around an imaginary rectangular box so you can easily center it, move it, and detect collisions
        self.screen_rect = screen.get_rect() # ensures the player does not get out of bounds

        self.rect.centerx = self.screen_rect.centerx # put the center of my ship at the center of the screen
        self.rect.bottom = self.screen_rect.bottom # put the bottom of my ship at the bottom of the screen

    def blitme(self):
        self.screen.blit(self.image, self.rect) # draws the image on the screen with the specified rect value