from datetime import date, datetime

POTENTIAL_CORRECT_GUESSES: int = 6


class GameStats:
    def __init__(self):
        self.game_type: str = ""
        self.daily_stats_dict: dict[str, int] = self.gen_stats_dict("stats/daily_stats.txt")
        self.random_stats_dict: dict[str, int] = self.gen_stats_dict("stats/random_stats.txt")
        self.combined_stats_dict: dict[str, int] = {}
        self.streak: int = 0
        self.gen_combined_dict()
        self.check_streak()

    def add_score(self, guesses: int):
        if self.game_type != "manual":
            # Writes score to stats file
            with open("stats/" + self.game_type + "_stats.txt", 'a') as fs:
                fs.write(str(guesses))
                self.gen_stats_dict("stats/" + self.game_type + "_stats.txt")

            # Updates dictionaries
            self.daily_stats_dict = self.gen_stats_dict("stats/daily_stats.txt")
            self.random_stats_dict = self.gen_stats_dict("stats/random_stats.txt")
            self.gen_combined_dict()

    def check_streak(self):
        # Read and store dates.txt
        with open("stats/dates.txt", "r") as fs:
            dates: list[str] = fs.readlines()

        # Check if streak has been broken
        if len(dates) > 0:
            days = (date.today() - datetime.strptime(dates[-1], "%Y-%m-%d").date()).days

            if days > 1:
                self.streak = 0
                self.clear_file("stats/dates.txt")
            else:
                self.streak = len(dates) - 1

        else:
            self.streak = 0

    def add_to_streak(self):
        with open("stats/dates.txt", "a") as fs:
            fs.write("\n" + str(date.today()))
        self.streak += 1

    def gen_combined_dict(self):
        for num_key in self.daily_stats_dict.keys():
            self.combined_stats_dict[num_key] = self.daily_stats_dict[num_key] + self.random_stats_dict[num_key]

    @staticmethod
    def gen_stats_dict(file: str) -> dict[str, int]:
        nums_list: list[str]
        # 1, 2, 3, 4, 5, 6, loss
        stats_list: list[int] = [0, 0, 0, 0, 0, 0, 0]
        stats_dict = {}

        # Splits file into single characters
        with open(file, 'r') as fs:
            nums_list = [*fs.read()]

        # Store values in appropriate indices
        for num in nums_list:
            stats_list[int(num) - 1] += 1

        # Store indices in dictionary
        for x in range(len(stats_list)):
            # Check for loss
            if x != 6:
                stats_dict.update({str(x + 1): stats_list[x]})
            else:
                stats_dict.update({"x": stats_list[x]})

        return stats_dict

    @staticmethod
    def average(stats_dict: dict[str, int]) -> float:
        guess_sum: int = 0
        guess_num: int = 0

        for num_key in stats_dict.keys():
            if num_key != "x":
                guess_sum += int(num_key) * stats_dict[num_key]
                guess_num += stats_dict[num_key]

        return guess_sum / guess_num

    @staticmethod
    def played_today() -> bool:
        # Stores dates as strings
        with open("stats/dates.txt", "r") as fs:
            dates_str = fs.read().split("\n")

        dates: list[datetime] = []

        # Converts strings to datetimes
        for day in dates_str:
            if day != "":
                dates.append(datetime.strptime(day, "%Y-%m-%d"))

        if len(dates) > 0:
            return dates[-1].date() == date.today()
        else:
            return False

    @staticmethod
    def clear_file(file: str):
        with open(file, "w") as fs:
            fs.write("")
