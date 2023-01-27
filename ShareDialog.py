from datetime import date
from PyQt5 import QtWidgets
from Row import Row
from UiShareDialog import UiShareDialog


class ShareDialog(UiShareDialog, QtWidgets.QDialog):
    def __init__(self):
        super(ShareDialog, self).__init__()
        self.setup_ui(self)
        self.ok_button.clicked.connect(self.accept)

    def generate_share_text(self, rows: tuple[Row, Row, Row, Row, Row, Row], guesses: int, game_type: str):
        share_text_lines: list[str] = [f'WordleQt {guesses}/6 {date.today()}', f'{game_type.capitalize()} game']

        for x in range(guesses):
            row_text = ""

            for char_box in rows[x].char_boxes:
                match char_box.get_status():
                    case "incorrect":
                        row_text += "⬛"
                    case "partial":
                        row_text += "🟨"
                    case "correct":
                        row_text += "🟩"

            share_text_lines.append(row_text)

        for line in share_text_lines:
            self.share_text.appendPlainText(line)
