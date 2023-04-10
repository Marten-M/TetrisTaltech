"""Constants in the game."""
import pygame
import os

file_dir = os.path.dirname(__file__)
fonts_path = os.path.join(os.path.dirname(file_dir), "fonts")
arcade_classic_font_path = os.path.join(fonts_path, "ARCADECLASSIC.TTF")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675

BLOCK_SIZE = 24

VERTICAL_TILES = 20
HORIZONTAL_TILES = 10

gFonts = {
    "smallFont": pygame.font.Font(arcade_classic_font_path, 16),
    "mediumFont": pygame.font.Font(arcade_classic_font_path, 32),
    "largeFont": pygame.font.Font(arcade_classic_font_path, 64),
    "veryLargeFont": pygame.font.Font(arcade_classic_font_path, 128)
}

gColors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "orange": (255, 165, 0),
    "gray": (128,128,128),
    "red": (255, 0, 0),
    "cyan": (0, 100, 100),
    "purple": (160, 32, 240),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0)
}
