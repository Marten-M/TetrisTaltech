"""Tetris blocks classes file."""
from pygame import Rect
from typing import Tuple, List

from .gameelement import GameElement
from .board import Board
from ..lib.screen import Screen
from ..constants import gColors, BLOCK_SIZE


class Block(GameElement):
    """Basic block class."""
    def __init__(self, x: int, y: int, color: str, tetromino_id: int, game_box: Rect, screen: Screen, board: Board):
        """
        Initialize block.

        :param x: x coordinate of block
        :param y: y coordinate of block
        :param color: color of the block
        :param tetromino_id: id of tetromino block is part of
        :param game_box: pygame Rect object of box the Block is in
        :param screen: Screen class for drawing objects
        """
        super().__init__()
        self.x = x
        self.y = y
        self.x_offset = game_box.x
        self.y_offset = game_box.y

        self.id = tetromino_id
        self.color = color
        self.screen = screen
        self.board = board

        self.cleared = False

    def force_move_down(self):
        """Forcefully move block down."""
        self.board[self.y][self.x] = 0
        self.y += 1
        self.board[self.y][self.x] = self

    def render(self):
        """
        Render block to screen
        """
        if not self.cleared:
            self.screen.graphics["color"] = gColors[self.color]
            self.screen.draw_box(BLOCK_SIZE, BLOCK_SIZE, self.x * BLOCK_SIZE + self.x_offset, self.y * BLOCK_SIZE + self.y_offset, fill=True)
    
    def __repr__(self) -> str:
        return self.color


class Tetromino(GameElement):
    """Base class for all tetrominos."""
    def __init__(self, x: int, y: int, color: str, id: int, board: Board, screen: Screen):
        """
        Initialize Tetromino class.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param color: color of the tetromino
        :param id: unique id of the tetromino
        :param board: board object of the board the tetromino is in
        :param screen: Screen object that draws tetrominos
        """
        super().__init__()

        self.main_x = x
        self.main_y = y

        self.id = id
        self.board = board
        self.color = color

        self.blocks: List[Block] = []
        self.screen = screen

        self.position = 1
        self.in_storage = False
        self.board.tetrominos[self.id] = self

    def move_right(self, amount: int = 1) -> bool:
        """
        Move tetromino right, if possible

        :param amount: how many tiles to move

        :return: boolean indicating wether the block was moved or not
        """
        self.blocks.sort(key=lambda x: -x.x)
        for block in self.blocks:
            if block.x + amount >= self.board.width or (self.board[block.y][block.x + amount] and self.board[block.y][block.x + amount].id != self.id):
                return False

        for block in self.blocks:
            self.board[block.y][block.x] = 0
            block.x += amount
            self.board[block.y][block.x] = block
        self.main_x += amount

        return True

    def move_left(self, amount: int = 1) -> bool:
        """
        Move tetromino left, if possible.

        :param amount: how many tiles to move

        :return: boolean indicating wether the block was moved or not
        """
        self.blocks.sort(key=lambda x: x.x)
        for block in self.blocks:
            if block.x - amount < 0 or (self.board[block.y][block.x - amount] and self.board[block.y][block.x - amount].id != self.id):
                return False

        for block in self.blocks:
            self.board[block.y][block.x] = 0
            block.x -= amount
            self.board[block.y][block.x] = block
        self.main_x -= amount

        return True

    def move_down(self, amount: int = 1) -> bool:
        """
        Move tetromino down, if possible.

        :param amount: how many tiles to move

        :return: boolean indicating wether the block was moved or not
        """
        self.blocks.sort(key=lambda x: -x.y)
        for block in self.blocks:
            if block.y < 0:
                continue
            elif block.y + amount >= self.board.height or (self.board[block.y + amount][block.x] and self.board[block.y + amount][block.x].id != self.id):
                return False

        for block in self.blocks:
            if block.y >= 0:
                self.board[block.y][block.x] = 0
            block.y += amount
            if block.y >= 0:
                self.board[block.y][block.x] = block
        self.main_y += amount

        return True

    def move_up(self, amount: int = 1):
        """
        Move tetromino up, if possible.

        :param amount: how many tiles to move

        :return: boolean indicating wether the block was moved or not
        """
        self.blocks.sort(key=lambda x: x.y)
        for block in self.blocks:
            if block.y - amount < 0 or (self.board[block.y - amount][block.x] and self.board[block.y - amount][block.x].id != self.id):
                return False

        for block in self.blocks:
            self.board[block.y][block.x] = 0
            block.y -= amount
            self.board[block.y][block.x] = block
        self.main_y -= amount

        return True

    def rotate_clockwise(self):
        """
        Rotate tetromino clockwise, if possible.

        :return: boolean indicating wether the block was moved or not
        """
        new_coords = [] # List of coordinates in the form [(x, y), (x, y)]
        for block in self.blocks:
            new_coords.append((self.main_x + self.main_y - block.y, block.x + self.main_y - self.main_x))
        for x, y in new_coords:
            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height or (self.board[y][x] and self.board[y][x].id != self.id):
                return False

        for block in self.blocks:
            self.board[block.y][block.x] = 0
        for i in range(len(self.blocks)):
            block = self.blocks[i]
            new_x, new_y = new_coords[i]
            block.x, block.y = new_x, new_y
            self.board[new_y][new_x] = block

        return True

    def rotate_counterclockwise(self):
        """
        Rotate tetromino counterclockwise, if possible.

        :return: boolean indicating wether the block was moved or not
        """
        new_coords = [] # List of coordinates in the form [(x, y), (x, y)]
        for block in self.blocks:
            new_coords.append((block.y + self.main_x - self.main_y, self.main_x + self.main_y - block.x))
        for x, y in new_coords:
            if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height or (self.board[y][x] and self.board[y][x].id != self.id):
                return False

        for block in self.blocks:
            self.board[block.y][block.x] = 0
        for i in range(len(self.blocks)):
            block = self.blocks[i]
            new_x, new_y = new_coords[i]
            block.x, block.y = new_x, new_y
            self.board[new_y][new_x] = block

        return True

    def render(self):
        """
        Render tetromino.
        """
        for block in self.blocks:
            block.render()

    def create_blocks(self, block_coords: List[Tuple[int, int]]):
        """
        Create blocks in tetromino given their coordinates.

        If a coordinate is already used, then the block will be spawned 3 levels higher.
        
        :param block_coords: list of coordinates in the form [(x, y), (x, y), ...]
        """
        can_spawn = True
        for x, y in block_coords:
            if self.board[y][x]:
                can_spawn = False
        
        for x, y in block_coords:
            if can_spawn:
                self.blocks.append(Block(x, y, self.color, self.id, self.board.rect, self.screen, self.board))
            else:
                self.blocks.append(Block(x, y - 3, self.color, self.id, self.board.rect, self.screen, self.board))


class IBlock(Tetromino):
    """I block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize I block.

        It is assumed creating a block is possible

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the I block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "cyan", id, board, screen)
        self.create_blocks([(x - 1, y), (x, y), (x + 1, y), (x + 2, y)])


class TBlock(Tetromino):
    """T block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize T block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the T block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "purple", id, board, screen)
        self.create_blocks([(x - 1, y), (x, y - 1), (x, y), (x + 1, y)])


class LBlock(Tetromino):
    """L block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize L block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the L block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "orange", id, board, screen)
        self.create_blocks([(x - 1, y), (x, y), (x + 1, y - 1), (x + 1, y)])


class ReverseLBlock(Tetromino):
    """Reverse L block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize reverse L block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the reverese L block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "blue", id, board, screen)
        self.create_blocks([(x - 1, y - 1), (x - 1, y), (x, y), (x + 1, y)])


class Squareblock(Tetromino):
    """Square block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize square block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the square block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "yellow", id, board, screen)
        self.create_blocks([(x, y - 1), (x, y), (x + 1, y - 1), (x + 1, y)])


class ZBlock(Tetromino):
    """Z block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize Z block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the Z block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "red", id, board, screen)
        self.create_blocks([(x - 1, y - 1), (x, y - 1), (x, y), (x + 1, y)])


class ReverseZBlock(Tetromino):
    """Z block class"""
    def __init__(self, x: int, y: int, id: int, board: Board, screen: Screen):
        """
        Initialize reverse Z block.

        It is assumed creating a block is possible.

        :param x: x coordinate of main block
        :param y: y coordinate of main block
        :param id: id of tetromino
        :param board: Board object of the board the reverse Z block is in
        :param screen: Screen object to draw blocks to the screen
        """
        super().__init__(x, y, "green", id, board, screen)
        self.create_blocks([(x - 1, y), (x, y - 1), (x, y), (x + 1, y - 1)])
