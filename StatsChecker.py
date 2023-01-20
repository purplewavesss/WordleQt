class StatsChecker:
    def __init__(self):
        self.game_type: str = ""

    def add_score(self, guesses: int):
        if self.game_type == "daily":
            with open("stats/daily_stats.txt", 'a') as fs:
                fs.write(str(guesses))

        elif self.game_type == "random":
            with open("stats/random_stats.txt", 'a') as fs:
                fs.write(str(guesses))
