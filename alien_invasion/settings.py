# Settings
#
# This class contains all the settings for Alien Invasion.


class Settings():
    """This class contains all the settings for the Alien Invasion game."""
    def __init__(self):
        """Initialize the games settings."""
        self.default_screen_width = 1200
        self.default_screen_height = 800
        self.fullscreen = False

        # Create screen size as a tuple.
        self.screen_size = (self.default_screen_width,
                            self.default_screen_height)
        self.bg_color = (230, 230, 230)

        self.caption = "Alien Invasion"
        # The ships speed is controlled by this attribute. The higher the
        # number, the faster it will go.
        self.ship_speed = 1.5
