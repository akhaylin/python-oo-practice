from random import choice


class WordFinder:
    """
    Word Finder: finds random words from a dictionary.

    >>> from random import seed
    >>> word_finder = WordFinder("test.txt")
    >>> seed(42)
    >>> word_finder.random()
    'hello'

    """

    def __init__(self, path):
        """
        Initialize a WordFinder instance by setting path and reading the file
        path points to and storing the words into self.words.
        Print the number of words read.
        """
        # print("Inside parent __init__")
        self.path = path
        self.words = self._read_file()
        self._log_words_read()

    def __repr__(self):
        if len(self.words) > 3:
            words_str = str(self.words[:3])[:-1] + '...]'
        else:
            words_str = self.words
        return f"<WordFinder path={self.path} word={words_str}>"

    def _read_file(self):
        """
        Read in file at self.path and return list of words from file.
        File should have one word per line.
        """
        # print("Inside parent _read_file")
        with open(self.path, "r") as file:
            return [line.strip() for line in file]

    def random(self):
        """Returns a random word from self.words."""

        return choice(self.words)

    def _log_words_read(self):
        """Prints the number of words read."""

        # print(f"{len(self.words)} words read")


class SpecialWordFinder(WordFinder):
    """
    Special Word Finder: finds random words from a dictionary, ignoring blank
    lines and comments (#).
    Subclass of WordFinder.

    """

    def _read_file(self):
        """
        Read in file at self.path and return list of words from file.
        Ignores comments (lines that start with "#") and blank lines.
        """
        # print("Inside child _read_file")
        words = super()._read_file()
        return [word for word in words if not word.startswith("#") and word != '']
