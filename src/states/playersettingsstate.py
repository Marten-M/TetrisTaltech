"""PlayerSettingsState class file."""

from .basestate import BaseState

class PlayerSettingsState(BaseState):
    """Class for managing the player settings state."""
    def __init__(self, screen) -> None:
        """Initialize state."""
        super().__init__(screen)