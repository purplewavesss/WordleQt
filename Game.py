import Word


# Encapuslates the game functions
class Game:
    def __init__(self, _words_tuple: tuple[Word, Word, Word, Word, Word, Word]):
        self.words_tuple: tuple[Word, Word, Word, Word, Word, Word] = _words_tuple
