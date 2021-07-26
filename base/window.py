# window.py: contains a dataclass of window properties.
import pygame
from dataclasses import dataclass

from .state_classes import MenuState, GameState


@dataclass
class Window:
    screen: pygame.Surface = None
    screen_width: int = 0
    screen_height: int = 0
    clock: pygame.time.Clock = None
    running: bool = True
    ms: float = 0
    dt: float = 0
    menu_state: MenuState = MenuState.Menu
    game_state: GameState = GameState.Paused
