"""Screen class file"""

import pygame
from src.constants import gFonts, gColors

class Screen:
    """Class for rendering objects to the screen."""
    def __init__(self, width: int, height: int) -> None:
        """
        Initialize screen.

        :param width: width of the screen in pixels
        :param height: height of the screen in pixels
        """
        # Initial graphics settings
        self.graphics = {
            "color": gColors["black"],
            "border-width": 2, 
            "font": "mediumFont"
            }
        self.display = self.create_display(width, height)
        pygame.display.update()

    def clear(self) -> None:
        """Clear the screen."""
        self.graphics["color"] = gColors["black"]
        self.display.fill(self.graphics["color"])

    def draw_text(self, text: str, x: int=0, y: int=0, text_align: str="center", *ignore, rect: pygame.Rect=None) -> None:
        """
        Draw text to specified coordinates.

        :param text: text to be drawn
        :param x: horizontal coordinate of text, if rect given then x coordinate relative to the rectangles top left corner
        :param y: vertical coordinate of middle point of text, if rect given then y coordinate relative to the rectangles top left corner
        :param rect: pygame Rect object to draw text into
        """
        font = gFonts[self.graphics["font"]]
        size = pygame.font.Font.size(font, text)

        if rect is not None:
            x += rect.left
            y += rect.top
        # change y
        y -= size[1] / 2
        # Change x
        if text_align == "center":
            x -= size[0] / 2
        elif text_align == "right":
            x += size[0] / 2

        # Draw text on screen
        self.display.blit(font.render(text, True, self.graphics["color"]), (x, y))

    def draw_box(self, width: int=0, height: int=0, x: int=0, y: int=0, *ignore, fill: bool=True, rect: pygame.Rect=None) -> pygame.Rect:
        """
        Draw a box with given dimensions on the screen and return the drawn rectangle.

        :param width: width of the box
        :param height: height of the box
        :param x: X coordinate of top left corner of the box
        :param y: Y coordinate of top left corner of the box
        :param fill: whether to fill the box or not
        :param rect: pygame Rect object to draw if one already created

        :param return: pygame Rect object of drawn rectangle
        """
        if rect is not None:
            rectangle = rect
        else:
            rectangle = pygame.Rect(x, y, width, height)

        if fill:
            pygame.draw.rect(self.display, self.graphics["color"], rectangle)
        else:
            pygame.draw.rect(self.display, self.graphics["color"], rectangle, self.graphics["border-width"])

        return rectangle

    def create_display(self, width: int, height: int):
        """
        Create display screen.

        :param width: width of the screen in pixels
        :param height: height of the screen in pixels
        """
        screen_dimensions = (width, height)
        screen = pygame.display.set_mode(size=screen_dimensions)

        pygame.display.set_caption("Tetris")
        # Fill screen with black
        screen.fill(gColors["black"])
        return screen