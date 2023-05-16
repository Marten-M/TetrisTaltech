"""TitleSceenState class file"""

import pygame
import sys

from .basestate import BaseState
from ..constants import gColors, gFonts, SCREEN_HEIGHT, SCREEN_WIDTH


class TitleScreenState(BaseState):
    """Class for managing actions on the title screen."""
    def __init__(self, screen) -> None:
        """Initialize state."""
        super().__init__(screen)
        self.create_boxes()
        self.current_selection = 0

    def update(self, dt: float) -> bool:
        """
        Update title screen state.
        
        :param dt: time since last frame in milliseconds
        :return: True if state needs to be changed, False otherwise
        """
        return self.handle_keyboard_input()

    def render(self):
        """
        Render title screen.
        """
        self.screen["color"] = gColors["white"]
        self.screen["font"] = gFonts["extremelyLargeFont"]
        # Game title
        self.screen.draw_text("T    TRIS", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, text_align="center")
        self.screen.draw_text("E", SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 4, text_align="center") # split apart because E looks weird when in 1 text

        # Buttons
        self.screen["font"] = gFonts["largeFont"]
        self.screen["border-width"] = 2
        # Draw play box
        self.set_selection_color(1)
        self.screen.draw_box(rect=self.play_box, fill=False)
        self.screen.draw_text("PLAY", self.play_box.width // 2, self.play_box.height // 2, text_align="center", rect=self.play_box)
        # Draw exit box
        self.set_selection_color(2)
        self.screen.draw_box(rect=self.exit_box, fill=False)
        self.screen.draw_text("EXIT", self.exit_box.width // 2, self.exit_box.height // 2, text_align="center", rect=self.exit_box)

    def create_boxes(self) -> None:
        """Create PlAY and EXIT boxes."""
        box_width = SCREEN_WIDTH * 0.4
        box_height = 60

        center_pos_horizontal = SCREEN_WIDTH / 2 - box_width / 2
        play_box_pos_vertical = SCREEN_HEIGHT / 2
        exit_box_pos_vertical = play_box_pos_vertical + (box_height + 20)

        self.play_box = pygame.Rect(center_pos_horizontal, play_box_pos_vertical, box_width, box_height)
        self.exit_box = pygame.Rect(center_pos_horizontal, exit_box_pos_vertical, box_width, box_height)

    def set_selection_color(self, target_value: int) -> None:
        """
        Set color of selection box.

        params:
        target_value - target value of self.current_selection in which case the box should be orange
        """
        if target_value == self.current_selection:
            self.screen["color"] = gColors["orange"]
        else:
            self.screen["color"] = gColors["white"]

    def handle_keyboard_input(self) -> None:
        """
        Get change of selected box.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.current_selection == 1:
                        return True
                    elif self.current_selection == 2:
                        pygame.quit()
                        sys.exit(0)
                    else:
                        self.current_selection = 1
                elif event.key in {pygame.K_DOWN, pygame.K_UP, pygame.K_w, pygame.K_s}:
                    self.current_selection = 1 if self.current_selection != 1 else 2
                elif event.key == pygame.K_ESCAPE:
                    self.current_selection = 0
                else:
                    self.current_selection = 1
        return False

    def exit(self) -> dict:
        """
        Exit the title screen state.

        :return: dictionary mapping the next state's entry params to values. one of the dictionary keys is always "state"
        """
        self.exit_params = {
                "state": "PlayerSettings",
            }
        return self.exit_params