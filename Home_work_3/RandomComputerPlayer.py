import random


class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    @staticmethod
    def get_move(game):
        square = random.choice(game.available_moves())
        return square
