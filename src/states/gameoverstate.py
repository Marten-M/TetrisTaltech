"""GameOverState class file."""

from .basestate import BaseState

class GameOverState(BaseState):
    """Class for managing the game over state."""
    def __init__(self, screen) -> None:
        """Initialize state."""
        super().__init__(screen)
