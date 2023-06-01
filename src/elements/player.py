"""Player class file."""
import pygame
from ..elements.blocks import Tetromino


class Player(object):
    """Player class."""
    def __init__(self, keys: dict):
        """
        Initialize player class.

        :param keys: dictionary mapping keys of the player
        """
        self.score = 0
        self.keys = keys

    def make_move(self, keypress, tetromino: Tetromino):
        """
        Make the move the player made.

        :param keypress: key the player pressed
        :param tetromino: Tetromino that is currently being moved
        """
        if keypress == self.keys["left"]:
            tetromino.move_left()
        if keypress == self.keys["right"]:
            tetromino.move_right()
        if keypress == self.keys["rotateLeft"]:
            tetromino.rotate_counterclockwise()
        if keypress == self.keys["rotateRight"]:
            tetromino.rotate_clockwise()
