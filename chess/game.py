import pygame
from pygame.constants import *

from dataclasses import dataclass

from base.window import Window, MenuState
from base.common import Color
from chess.chess_entities import Grid


@dataclass
class GameSystem:
    grid: Grid = None


def initialize(window: Window, g_sys: GameSystem):
    window.screen = pygame.display.get_surface()
    window.clock = pygame.time.Clock()
    window.screen_width = window.screen.get_width()
    window.screen_height = window.screen.get_height()

    g_sys.grid = Grid(window.screen_width, window.screen_height,
                      Color.Gray, Color.Coffee)


def event_loop(window: Window, g_sys: GameSystem):
    for event in pygame.event.get():
        if event.type == QUIT:
            window.menu_state = MenuState.Quit

        if event.type == KEYDOWN:
            pass


def update(window: Window, g_sys: GameSystem):
    window.dt = window.ms / 1000.0
    pass


def draw(window: Window, g_sys: GameSystem):
    window.screen.fill([235, 235, 235])

    g_sys.grid.draw_to(window.screen)

    pygame.display.update()
