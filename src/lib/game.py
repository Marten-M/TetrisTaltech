"""Game class file."""

import pygame

from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .screen import Screen

from ..states.basestate import BaseState
from ..states.titlescreenstate import TitleScreenState
from ..states.playersettingsstate import PlayerSettingsState
from ..states.playstate import PlayState
from ..states.gameoverstate import GameOverState

class Game(object):
    """Class for running and managing the game."""
    def __init__(self, initial_state: str) -> None:
        """
        Initialize game class.

        :param initial_state: inital state of the game to enter
        """
        pygame.init()
        self.states = {
            "TitleScreen": TitleScreenState,
            "PlayerSettings": PlayerSettingsState,
            "Play": PlayState,
            "GameOver": GameOverState
        }
        self.state: BaseState = self.states[initial_state]()
        self.screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()

    def change_state(self, *ignore, params: dict=dict()) -> None:
        """
        Change game state.

        :param new_state: new state to enter
        """
        params |= self.state.exit()
        new_state = params.pop('state')
        self.state: BaseState = self.states[new_state](self.screen)
        self.state.enter(params)

    def run(self) -> None:
        """
        Run the game.
        """
        cur_time = 0
        fps = int(self.clock.get_fps())
        while True:
            # Udate state
            dt = self.clock.tick()
            cur_time += dt / 1000
            if self.state.update(dt):
                self.change_state()
                continue
            # Render to screen
            self.screen.clear()
            self.state.render()

            if cur_time >= 0.4: # update fps every 0.4 seconds
                cur_time = 0
                fps = int(self.clock.get_fps())

            if self.state.drawFPS:
                self.screen.graphics["color"] = "white"
                self.screen.graphics["font"] = "mediumFont"
                self.screen.draw_text(f"{fps} FPS", 10, 10, text_align="left")

            pygame.display.update()
