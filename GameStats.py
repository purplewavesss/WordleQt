POTENTIAL_CORRECT_GUESSES: int = 6


class GameStats:
    def __init__(self):
        self.game_type: str = ""
        self.stats_dict: dict[str, int] = {}
        self.gen_stats_dict()

    def add_score(self, guesses: int):
        if self.game_type == "daily":
            with open("stats/daily_stats.txt", 'a') as fs:
                fs.write(str(guesses))
                self.gen_stats_dict()

        elif self.game_type == "random":
            with open("stats/random_stats.txt", 'a') as fs:
                fs.write(str(guesses))
                self.gen_stats_dict()

    def gen_stats_dict(self):
        nums_list: list[str]
        # 1, 2, 3, 4, 5, 6, loss
        stats_list: list[int] = [0, 0, 0, 0, 0, 0, 0]
        self.stats_dict = {}

        with open("stats/random_stats.txt", 'r') as fs:
            nums_list = fs.read().split()

        for num in nums_list:
            stats_list[int(num) - 1] += 1

        for x in range(len(stats_list)):
            if x != 6:
                self.stats_dict.update({str(x + 1): stats_list[x]})
            else:
                self.stats_dict.update({"x": stats_list[x]})

    def average(self) -> float:
        guess_sum: int = 0
        guess_num: int = 0

        for num_key in self.stats_dict.keys():
            if num_key != "x":
                guess_sum += int(num_key) * self.stats_dict[num_key]
                guess_num += self.stats_dict[num_key]

        return guess_sum / guess_num
