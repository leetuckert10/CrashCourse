# Alien Invasion Version 1.0

import sys
import pygame
import settings
import ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create the resources."""
        pygame.init()

        self.settings = settings.Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption(self.settings.caption)

        self.ship = ship.Ship(self)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self) -> None:
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: object) -> None:
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self._set_fullscreen_mode()

    def _check_keyup_events(self, event: object) -> None:
        """Respond to key releases."""
        if pygame.K_RIGHT == event.key:
            self.ship.moving_right = False
        elif pygame.K_LEFT == event.key:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen."""

        # Set the background color.
        self.screen.fill(self.settings.bg_color)

        # Draw the ship.
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _set_fullscreen_mode(self):
        """The method allows the user to toggle back and forth between
        fullscreen mode and the default size defined in settings."""
        if self.settings.fullscreen:
            self.settings.screen_size = (self.settings.default_screen_width,
                                         self.settings.default_screen_height)
            self.screen = pygame.display.set_mode(self.settings.screen_size)
            self.settings.fullscreen = False
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.fullscreen = True

        # We use this attribute to keep the ship from going off the screen so
        # we must keep updated.
        self.ship.screen_rect = self.screen.get_rect()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
