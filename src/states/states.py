"""Global states file."""

from .titlescreenstate import TitleScreenState
from .playersettingsstate import PlayerSettingsState
from .playstate import PlayState
from .gameoverstate import GameOverState


gStates = {
    "TitleScreen": TitleScreenState,
    "PlayerSettings": PlayerSettingsState,
    "Play": PlayState,
    "GameOver": GameOverState
}

