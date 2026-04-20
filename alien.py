import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Creates a class to house bullets for the arsenal"""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initializes a function for the bullets in the arsenal"""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.rotate(self.image, (90))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Updates the alien's location"""
        temp_speed = self.settings.fleet_speed

        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self):
        """Checks the edges and stops alien when it reaches an edge"""
        return (self.rect.top <= self.boundaries.top or self.rect.bottom >= self.boundaries.bottom)

    def draw_alien(self):
        """Draws the alien on the screen"""
        self.screen.blit(self.image, self.rect)