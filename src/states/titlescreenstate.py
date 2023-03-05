"""TitleSceenState class file"""

import pygame

from .basestate import BaseState

class TitleScreenState(BaseState):
    """Class for managing actions on the title screen."""
    def __init__(self, screen) -> None:
        """Initialize state."""
        super().__init__(screen)

    def update(self, dt: float) -> bool:
        """
        Update title screen state.
        
        :param dt: time since last frame in milliseconds
        :return: True if state needs to be changed, False otherwise
        """
        for event in pygame.event.get():
            pass
        return False