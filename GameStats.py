POTENTIAL_CORRECT_GUESSES: int = 6


class GameStats:
    def __init__(self):
        self.game_type: str = ""
        self.daily_stats_dict: dict[str, int] = self.gen_stats_dict("stats/daily_stats.txt")
        self.random_stats_dict: dict[str, int] = self.gen_stats_dict("stats/random_stats.txt")
        self.combined_stats_dict: dict[str, int] = {}
        self.gen_combined_dict()

    def add_score(self, guesses: int):
        with open("stats/" + self.game_type + "_stats.txt", 'a') as fs:
            fs.write(str(guesses))
            self.gen_stats_dict("stats/" + self.game_type + "_stats.txt")
        self.daily_stats_dict = self.gen_stats_dict("stats/daily_stats.txt")
        self.random_stats_dict = self.gen_stats_dict("stats/random_stats.txt")
        print(self.daily_stats_dict)
        self.gen_combined_dict()

    @staticmethod
    def gen_stats_dict(file: str) -> dict[str, int]:
        nums_list: list[str]
        # 1, 2, 3, 4, 5, 6, loss
        stats_list: list[int] = [0, 0, 0, 0, 0, 0, 0]
        stats_dict = {}

        with open(file, 'r') as fs:
            nums_list = [*fs.read()]

        for num in nums_list:
            stats_list[int(num) - 1] += 1

        for x in range(len(stats_list)):
            if x != 6:
                stats_dict.update({str(x + 1): stats_list[x]})
            else:
                stats_dict.update({"x": stats_list[x]})

        return stats_dict

    def gen_combined_dict(self):
        for num_key in self.daily_stats_dict.keys():
            self.combined_stats_dict[num_key] = self.daily_stats_dict[num_key] + self.random_stats_dict[num_key]

    @staticmethod
    def average(stats_dict: dict[int, str]) -> float:
        guess_sum: int = 0
        guess_num: int = 0

        for num_key in stats_dict.keys():
            if num_key != "x":
                guess_sum += int(num_key) * stats_dict[num_key]
                guess_num += stats_dict[num_key]

        return guess_sum / guess_num
