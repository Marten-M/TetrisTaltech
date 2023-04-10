"""Board class file."""
import pygame

from .gameelement import GameElement
from ..constants import VERTICAL_TILES, HORIZONTAL_TILES, BLOCK_SIZE

class Board(GameElement):
    """Board class."""
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize board.

        :param x: x coordinate of board's top left corner
        :param y: y coordinate of board's top left corner
        """
        super().__init__()
        self.x = x
        self.y = y
        
        self.width = HORIZONTAL_TILES
        self.height = VERTICAL_TILES
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        self.rect = pygame.rect.Rect(x, y, self.width * BLOCK_SIZE, self.height * BLOCK_SIZE)

    def __getitem__(self, y: int) -> list:
        """
        Get board row.
        """
        return self.board[y]



    
