"""Board class file."""
import pygame
import time

from .gameelement import GameElement
from ..lib.screen import Screen
from ..constants import VERTICAL_TILES, HORIZONTAL_TILES, BLOCK_SIZE, gColors, gFonts, SCREEN_WIDTH, SCREEN_HEIGHT

class Board(GameElement):
    """Board class."""
    def __init__(self, x: int, y: int, screen: Screen) -> None:
        """
        Initialize board.

        :param x: x coordinate of board's top left corner
        :param y: y coordinate of board's top left corner
        :param screen: Screen class object for drawing to the screen
        """
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        
        self.width = HORIZONTAL_TILES
        self.height = VERTICAL_TILES
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]

        self.rect = pygame.rect.Rect(x, y, self.width * BLOCK_SIZE, self.height * BLOCK_SIZE)
        self.tetrominos = {}
        self.cleared_rows = 0
        self.level = 1
        self.player_score = 0


    def update_board(self):
        """Remove all cleared rows and move every block above them down."""
        removed_rows = []
        for y in range(self.height - 1, -1, -1):
            row = self.board[y]
            if row.count(0) == 0:
                removed_rows.append(y)
                self.clear_row(y)

        for y in removed_rows[::-1]:
            for other_y in range(y - 1, -1, -1):
                for block in self.board[other_y]:
                    if block:
                        block.force_move_down()
        

    def clear_row(self, row: int):
        """
        Clear a given row of blocks and move all other blocks down.

        :param row: row to clear
        """
        blocks = self.board[row]
        for i in range(self.width):
            block = blocks[i]
            blocks[i] = 0
            block.cleared = True
        self.cleared_rows += 1


    def detect_loss(self) -> bool:
        """
        Detect whether the game was lost or not.
        
        :return: boolean indicating whether the game was lost or not.
        """
        for key in self.tetrominos:
            tetro = self.tetrominos[key]
            for block in tetro.blocks:
                if block.y < 0:
                    return True
        return False

    def render(self):
        """Render the board and all its blocks."""
        # Gridlines
        self.screen["color"] = gColors["dark_gray"]
        for i in range(HORIZONTAL_TILES):
            self.screen.draw_box(1, VERTICAL_TILES * BLOCK_SIZE, self.rect.left + BLOCK_SIZE * i, self.rect.top)
        for i in range(VERTICAL_TILES):    
            self.screen.draw_box(HORIZONTAL_TILES * BLOCK_SIZE, 1, self.rect.left, self.rect.top + BLOCK_SIZE * i)
        # Render blocks
        for id in self.tetrominos:
            self.tetrominos[id].render()
        # Render board border
        self.screen["color"] = gColors["white"]
        self.screen["border-width"] = 2
        self.screen.draw_box(fill=False, rect=self.rect)
        # Render player level
        self.screen["color"] = gColors["white"]
        self.screen["font"] = gFonts["mediumFont"]
        self.screen.draw_text(f"LEVEL {self.level}", 1190, 20, text_align="right")
        # Render the Player's score
        self.screen["color"] = gColors["white"]
        self.screen["font"] = gFonts["mediumFont"]
        self.screen.draw_text(f"{self.player_score} POINTS", 1190, 50, text_align="right")
        

    def __getitem__(self, y: int) -> list:
        """
        Get board row.
        """
        return self.board[y]



    
