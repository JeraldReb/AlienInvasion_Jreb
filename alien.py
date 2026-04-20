import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """Creates a class to house bullets for the arsenal"""

    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        """Initializes a function for the bullets in the arsenal"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.rotate(self.image, (90))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # self.x = float(self.rect.x)

    def update(self):
        """Updates the bullets as they are fired"""
        pass

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)