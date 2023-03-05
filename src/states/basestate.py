"""Base state class file."""

from ..lib.screen import Screen


class BaseState(object):
    """
    Base state with empty functions for the games different states.
    """
    def __init__(self, screen: Screen) -> None:
        """Initialize base class."""
        self.drawFPS = True # Draw FPS by default
        self.screen = screen

    def enter(self, params: dict=dict()) -> None:
        """
        Gets called when game state is changed to this state.

        :param params: dictionary containing parameters to enter state with
        """
        pass


    def update(self, dt: float) -> bool:
        """
        The function that is called every frame. Game logic should be included here.

        :param dt: time in milliseconds since last frame
        :return: boolean indicating whether the state should change
        """
        pass

    def render(self) -> None:
        """
        The function that renders everything to the screen.
        """
        pass

    def debug(self) -> None:
        """
        Gets called when debug mode is enabled.
        """
        pass
    
    def exit(self) -> dict:
        """
        Exit function gets called when state is exited.

        :return: dictionary containing exit parameters
        """
        return dict()
