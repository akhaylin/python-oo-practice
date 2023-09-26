from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

def __init__(self, path):
    self.path = path
    self.words = self.read_file(path)

def read_file(self):
    with open(self.path, "r") as file:
        return [line.strip() for line in file]

def random(self):
    return choice(self.words)




