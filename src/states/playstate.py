"""PlayState class file."""

from .basestate import BaseState

class PlayState(BaseState):
    """Class for managin the play state."""
    def __init__(self, screen) -> None:
        """Initialize state."""
        super().__init__(screen)
