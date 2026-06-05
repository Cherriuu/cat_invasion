# source venv/bin/activate to go back into pygame virtual environment
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (168, 122, 242)
        self.ship_speed_factor = 1.8 # to move 1.8 pixels per key held
        self.mouse_speed_factor = 1

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        self.fleet_drop_speed = 50
        self.fleet_direction = 1 # 1 to the right

        self.cat_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        self.mouse_points = 50
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.cat_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.mouse_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.cat_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.mouse_speed_factor *= self.speedup_scale
        self.mouse_points = int(self.mouse_points * self.score_scale)