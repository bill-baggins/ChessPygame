import pygame
from pygame.constants import *

from dataclasses import dataclass

from base.window import Window, MenuState
from base.common import Color, GameFont, MouseButton
from chess.menu_entities import MainMenu, OptionMenu


@dataclass
class MenuSystem:
    main_menu: MainMenu = MainMenu()
    option_menu: OptionMenu = OptionMenu()


def initialize(window: Window, m_sys: MenuSystem):
    window.screen = pygame.display.get_surface()
    window.screen_width = window.screen.get_width()
    window.screen_height = window.screen.get_height()
    window.clock = pygame.time.Clock()
    window.screen_width = window.screen.get_width()
    window.screen_height = window.screen.get_height()

    main_menu = m_sys.main_menu
    main_menu.init_entities(window)
    main_menu.init_entity_list()

    option_menu = m_sys.option_menu
    option_menu.init_entities(window)
    option_menu.init_entity_list()


def event_loop(window: Window, m_sys: MenuSystem):
    for event in pygame.event.get():
        if event.type == QUIT:
            window.menu_state = MenuState.Quit

        if event.type == KEYDOWN:
            pass

        if event.type == MOUSEBUTTONDOWN:
            if event.button == MouseButton.Left:
                mouse_pos = pygame.mouse.get_pos()
                m_sys.main_menu.listen_for_button_events(mouse_pos, window)


def update(window: Window, m_sys: MenuSystem):
    window.dt = window.ms / 1000.0


def draw(window: Window, m_sys: MenuSystem):
    window.screen.fill(Color.Silver)

    if window.menu_state == MenuState.Menu:
        for ent in m_sys.main_menu.entities:
            ent.draw_to(window.screen)
    elif window.menu_state == MenuState.Options:
        pass

    pygame.display.update()
