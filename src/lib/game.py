"""Game class itself."""

class Game(object):
    """Class for running and managing the game."""
    def __init__(self, initial_state: str) -> None:
        """
        Initialize game class.

        :param initial_state: inital state of the game to enter
        """
        pass

    def change_state(self, new_state: str, *ignore, params: dict=dict()) -> None:
        """
        Change game state.

        :param new_state: new state to enter
        """
        pass

    def run(self) -> None:
        """
        Run the game.
        """
        pass