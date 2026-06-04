import pygame

class Cat():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/Kittycat.bmp') # load the image in and save it to self.image
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect() # .get_rect wraps the image around an imaginary rectangular box so you can easily center it, move it, and detect collisions
        self.screen_rect = screen.get_rect() # ensures the player does not get out of bounds

        self.rect.centerx = self.screen_rect.centerx # put the center of my ship at the center of the screen
        self.rect.bottom = self.screen_rect.bottom # put the bottom of my ship at the bottom of the screen

        self.center = float(self.rect.centerx) # store position of ship more accurately with decimals

        self.moving_right = False # a flag to detect if the user is continuosuly pressing down on the right button
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect) # draws the image on the screen with the specified rect value

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: # make sure the ship doesnt go out of bounds
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center