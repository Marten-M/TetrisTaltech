"""PlayerSettingsState class file. THIS STATE IS DROPPED."""

import pygame

from .basestate import BaseState
from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT, gColors, gFonts


class PlayerSettingsState(BaseState):
    """Class for managing the player settings state."""
    def __init__(self, screen):
        """Initialize state."""
        super().__init__(screen)
        self.create_boxes()
        self.current_selection = 1
        self.exit_state = False

    def update(self, dt: float) -> bool:
        """
        Update player settings state.
        
        :param dt: time since last frame in milliseconds
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.handle_keyboard_input(event.key)

        return self.exit_state


    def render(self):
        """Render player settings."""
        self.screen["color"] = gColors["white"]
        self.screen["font"] = gFonts["largeFont"]
        self.screen["border-width"] = 2
        # 1 player box
        self.set_selection_color(1)
        self.screen.draw_box(rect=self.one_player_box, fill=False)
        self.screen.draw_text("1 PLAYER", self.one_player_box.width // 2, self.one_player_box.height // 2, text_align="center", rect=self.one_player_box)
        # 2 player box
        self.set_selection_color(2)
        self.screen.draw_box(rect=self.two_player_box, fill=False)
        self.screen.draw_text("2 PLAYERS", self.two_player_box.width // 2, self.two_player_box.height // 2, text_align="center", rect=self.two_player_box)
        # BACK box
        self.set_selection_color(3)
        self.screen.draw_box(rect=self.back_box, fill=False)
        self.screen.draw_text("BACK", self.back_box.width // 2, self.back_box.height // 2, text_align="center", rect=self.back_box)

    def exit(self) -> dict:
        """Exit player settings state."""
        if self.current_selection == 3:
            self.exit_params["state"] = "TitleScreen"
        else:
            self.exit_params["state"] = "Play"
            self.exit_params["players"] = 1 if self.current_selection == 1 else 2
        
        return self.exit_params

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

    def create_boxes(self) -> None:
        """Create player selection and BACK boxes."""
        box_width = SCREEN_WIDTH * 0.4
        box_height = 60

        center_pos_horizontal = SCREEN_WIDTH / 2 - box_width / 2
        two_player_vertical = SCREEN_HEIGHT / 2
        one_player_vertical = two_player_vertical - (box_height + 20)
        back_box_vertical = two_player_vertical + (box_height + 20)

        self.one_player_box = pygame.Rect(center_pos_horizontal, one_player_vertical, box_width, box_height)
        self.two_player_box = pygame.Rect(center_pos_horizontal, two_player_vertical, box_width, box_height)
        self.back_box = pygame.Rect(center_pos_horizontal, back_box_vertical, box_width, box_height)

    def handle_keyboard_input(self, key):
        if key == pygame.K_RETURN:
            self.exit_state = True
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.current_selection = self.current_selection + 1 if self.current_selection + 1 <= 3 else 1
        elif key == pygame.K_UP or key == pygame.K_w:
            self.current_selection = self.current_selection - 1 if self.current_selection - 1 > 0 else 3
