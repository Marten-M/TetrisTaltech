"""Constants in the game."""
import pygame
import os

file_dir = os.path.dirname(__file__)
fonts_path = os.path.join(os.path.dirname(file_dir), "fonts")
arcade_classic_font_path = os.path.join(fonts_path, "ARCADECLASSIC.TTF")

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
    "red": (255, 0, 0)
}
