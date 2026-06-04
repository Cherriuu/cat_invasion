# source venv/bin/activate to go back into pygame virtual environment
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (168, 122, 242)
        self.ship_speed_factor = 1.5 # to move 1.5 pixels per key held

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)