"""PlayState class file."""

from ..lib.screen import Screen
from .basestate import BaseState

class PlayState(BaseState):
    """Class for managing the play state."""
    def __init__(self, screen: Screen):
        """Initialize state."""
        super().__init__(screen)

    def enter(self, params: dict):
        """Enter the play state."""
        self.players = params["players"]
    
    def update(self, dt: float) -> bool:
        """Update the play state every frame."""
        
