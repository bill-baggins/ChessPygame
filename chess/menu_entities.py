from dataclasses import dataclass
from typing import Callable

from base.common import Color, GameFont
from base.gui import TextBox, Button
from base.family import Family
from base.window import Window
from base.state_classes import MenuState


@dataclass
class MainMenu(Family):
    title_textbox: TextBox = None
    start_button: Button = None
    option_button: Button = None
    quit_button: Button = None

    def __start_button_action(self, window: Window) -> None:
        window.menu_state = MenuState.Game

    def __option_button_action(self, window: Window) -> None:
        window.menu_state = MenuState.Options

    def __quit_button_action(self, window: Window) -> None:
        window.menu_state = MenuState.Quit

    def init_entities(self, window: Window) -> None:
        self.title_textbox = TextBox(pos=[0, 0],
                                     size=[200, 50],
                                     background_color=Color.Silver,
                                     text="Chess",
                                     font=GameFont.Title,
                                     text_color=Color.Black,
                                     text_size=20)

        self.title_textbox.update_text_pos()
        self.title_textbox.set_pos([window.screen_width // 2 - self.title_textbox.width // 2, 20])

        self.start_button = Button(pos=[0, 0],
                                   size=[100, 40],
                                   background_color=Color.RayWhite,
                                   font=GameFont.Default,
                                   text="Start",
                                   text_size=20,
                                   text_color=Color.Black,
                                   action=self.__start_button_action)
        self.start_button.update_text_pos()
        self.start_button.set_pos([window.screen_width // 2 - self.start_button.width // 2, 140])

    def listen_for_button_events(self, mouse_pos: tuple, window: Window) -> None:
        for ent in self.entities:
            if isinstance(ent, Button):
                possible_event = ent.on_click(mouse_pos)
                if callable(possible_event):
                    possible_event(window)


class OptionMenu(Family):
    sounds_button: Button = None
    mm_button: Button = None

    def init_entities(self, window: Window):
        pass
