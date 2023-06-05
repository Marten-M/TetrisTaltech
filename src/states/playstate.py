"""PlayState class file."""

import random
import pygame

from ..lib.screen import Screen
from ..elements.board import Board
from .basestate import BaseState
from ..elements.blocks import Tetromino, LBlock, TBlock, IBlock, ZBlock, ReverseLBlock, ReverseZBlock, Squareblock
from ..constants import BLOCK_SIZE, VERTICAL_TILES, HORIZONTAL_TILES, SCREEN_WIDTH, SCREEN_HEIGHT


class PlayState(BaseState):
    """Class for managing the play state."""
    def __init__(self, screen: Screen):
        """Initialize state."""
        super().__init__(screen)
        self.board = Board(SCREEN_WIDTH // 2 - HORIZONTAL_TILES // 2 * BLOCK_SIZE, SCREEN_HEIGHT // 2 - VERTICAL_TILES // 2 * BLOCK_SIZE, self.screen)
        self.block_fall_speed_ms = 600 # How many milliseconds to wait before block falls down by 1
        self.block_fall_multiplier = 1.3 # How much the falling speeds up after every cleared row
        self.cleared_rows = 0 # Used to check the change of self.board.cleared_rows
        self.blocks = [LBlock, TBlock, IBlock, ZBlock, ReverseLBlock, ReverseZBlock, Squareblock]
        # Get first block that falls
        self.block_count = 0
        self.falling_block = self.get_new_falling_block()
        self.cur_timer_ms = 0

    def speedup(self):
        """Speed up the dropping of blocks"""
        if self.cleared_rows != self.board.cleared_rows:
            rows_cleared_at_once = 0
            while self.cleared_rows != self.board.cleared_rows:
                self.cleared_rows += 1
                rows_cleared_at_once += 1
                self.block_fall_speed_ms = round(self.block_fall_speed_ms / self.block_fall_multiplier)
            self.level_up()
            self.score(rows_cleared_at_once)

    def level_up(self):
        """Increase Players levels for every 5*(current level) rows cleared"""
        if self.cleared_rows >= 5*self.board.level:
            self.board.level += 1

    def score(self, rows):
        """Add points to the player score according to level and cleared rows"""
        self.board.player_score += rows ** 2 * self.board.level

    def update(self, dt: float) -> bool:
        """Update the play state every frame."""
        # Move block down, if that's what should happen
        self.cur_timer_ms += dt
        if self.cur_timer_ms >= self.block_fall_speed_ms:
            self.cur_timer_ms = 0

            if not self.falling_block.move_down(1):
                self.board.update_board()
                self.speedup()
                loss = self.board.detect_loss()
                self.falling_block = self.get_new_falling_block()
                return loss

        for event in pygame.event.get():
            if event.type == pygame.KEYUP: # If a keyboard button was depressed
                if event.key == pygame.K_m:
                    self.block_fall_speed_ms *= 4

            if event.type == pygame.KEYDOWN: # If a keyboard button was pressed
                if event.key == pygame.K_LEFT:
                    self.falling_block.move_left(1)
                elif event.key == pygame.K_RIGHT:
                    self.falling_block.move_right(1)
                elif event.key == pygame.K_UP:
                    self.falling_block.rotate_counterclockwise()
                elif event.key == pygame.K_DOWN:
                    self.falling_block.rotate_clockwise()
                elif event.key == pygame.K_m:
                    self.block_fall_speed_ms /= 4
                elif event.key == pygame.K_SPACE:
                    while self.falling_block.move_down(1):
                        pass

        return False

    def render(self):
        """Render the play state."""
        # Render the board and blocks
        self.board.render()

    def exit(self) -> dict:
        """Exit the play state."""
        self.exit_params["state"] = "GameOver"
        self.exit_params["board"] = self.board
        
        return self.exit_params

    def get_new_falling_block(self) -> Tetromino:
        """
        Get a random block out of all possible blocks.
        """
        self.block_count += 1
        return random.choice(self.blocks)(HORIZONTAL_TILES // 2, 1, self.block_count, self.board, self.screen)
