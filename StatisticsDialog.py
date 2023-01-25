from PyQt5 import QtWidgets
from GameStats import GameStats
from GameWindow import GameWindow
from UiStatisticsDialog import UiStatisticsDialog


class StatisticsDialog(QtWidgets.QDialog, UiStatisticsDialog):
    def __init__(self, _game_stats: GameStats, _data_type: str):
        super(StatisticsDialog, self).__init__()
        self.setup_ui(self)
        self.game_stats = _game_stats
        self.data_type: str = _data_type
        self.stats_dict: dict[str, int] = self.get_dict()
        self.setWindowTitle(self.data_type + " Statistics")
        self.gen_histogram()

    def get_dict(self) -> dict[str, int]:
        match self.data_type:
            case "Daily":
                return self.game_stats.daily_stats_dict
            case "Practice":
                return self.game_stats.random_stats_dict
            case "Combined":
                return self.game_stats.combined_stats_dict

    def gen_histogram(self):
        can_show_stats: bool = False

        for value in self.stats_dict.values():
            if value > 0:
                can_show_stats = True
                break

        if can_show_stats:
            values: list[int] = list(self.stats_dict.values())
            max_value = max(values)

            for x in range(len(self.histogram_bars)):
                self.histogram_bars[x].setToolTip(str(values[x]))
                if (values[x] / max_value) != 0:
                    self.histogram_bars[x].set_percentage(values[x] / max_value)

        else:
            GameWindow.gen_message_box("No statistics!", "There are no statistics to show!",
                                       QtWidgets.QMessageBox.Icon.Critical)
