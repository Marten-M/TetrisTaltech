"""GameOverState class file."""

from .basestate import BaseState

from ..constants import gColors, gFonts, BLOCK_SIZE, HORIZONTAL_TILES, SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverState(BaseState):
    """Class for managing the game over state."""
    def __init__(self, screen):
        """Initialize state."""
        super().__init__(screen)

    def enter(self, params: dict):
        """Enter the game over state."""
        self.board = params["board"]
    
    def update(self, dt: float) -> bool:
        """Update the game over state."""

    def render(self):
        """Render the game over state."""
        # Render the board
        self.board.render()

        # Render the game over text
        self.screen["color"] = gColors["white"]
        self.screen["font"] = gFonts["largeFont"]
        self.screen.draw_text("GAME OVER", (SCREEN_WIDTH + (self.board.rect.x + self.board.rect.width)) // 2, SCREEN_HEIGHT // 2 - 50)
        # Render the press enter to return to title screen text
        self.screen["font"] = gFonts["mediumFont"]
        self.screen.draw_text("Press", (SCREEN_WIDTH + (self.board.rect.x + self.board.rect.width)) // 2, SCREEN_HEIGHT // 2)
        self.screen["font"] = gFonts["largeFont"]
        self.screen.draw_text("ENTER", (SCREEN_WIDTH + (self.board.rect.x + self.board.rect.width)) // 2, SCREEN_HEIGHT // 2 + 35)
        self.screen["font"] = gFonts["mediumFont"]
        self.screen.draw_text("to   return  to    title   screen", (SCREEN_WIDTH + (self.board.rect.x + self.board.rect.width)) // 2, SCREEN_HEIGHT // 2 + 75)
