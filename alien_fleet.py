import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Creates a class to house the alien fleet"""

    def __init__(self, game: 'AlienInvasion'):
        """Initializes the alien fleet"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Creates the alien fleet"""
        alien_h = self.settings.alien_h
        alien_w = self.settings.alien_w
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w

        fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, alien_w, screen_w)
        
        half_screen = self.settings.screen_w//2
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_h
        y_offset = int((screen_h - fleet_vertical_space)//2)
        x_offset = int((half_screen - fleet_horizontal_space)//2)

        for col in range(fleet_w):
            for row in range(fleet_h):
                current_y = alien_h * row + y_offset
                current_x = alien_w * col + x_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_y, current_x)

    def calculate_fleet_size(self, alien_h, screen_h, alien_w, screen_w):
        """Calculates the possible size of the alien fleet"""
        fleet_h = (screen_h//alien_h)
        fleet_w = ((screen_w / 2)//alien_w)

        if fleet_h % 2 == 0:
            fleet_h -= 1

        else: 
            fleet_h -=2

        if fleet_w % 2 == 0:
            fleet_w -= 1

        else:
            fleet_w -= 2

        return int(fleet_h), int(fleet_w)

    def _create_alien(self, current_y: int, current_x: int):
        """Creates aliens within the fleet"""
        new_alien = Alien(self, current_y, current_x)

        self.fleet.add(new_alien)

    def draw(self):
        """Draws the alien fleet onscreen"""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()