class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats() # runs automatically whenever you create a gamestats object
        self.game_active = False # flag
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.cats_left = self.ai_settings.cat_limit
        self.score = 0