from dataclasses import dataclass

from base.common import Color, GameFont
from base.gui import TextBox, Button
from base.family import Family
from base.window import Window
from base.state_classes import MenuState


@dataclass
class MainMenuFamily(Family):
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
                                     text_color=Color.Black,
                                     text_size=50)

        self.title_textbox.update_text_pos()
        self.title_textbox.set_pos([window.screen_width // 2 - self.title_textbox.width // 2, 20])

        self.start_button = Button(pos=[0, 0],
                                   size=[200, 50],
                                   background_color=Color.RayWhite,
                                   text="Start",
                                   text_size=20,
                                   text_color=Color.Black,
                                   action=self.__start_button_action)
        self.start_button.update_text_pos()
        self.start_button.set_pos([window.screen_width // 2 - self.start_button.width // 2, 140])

        self.option_button = Button(pos=[0, 0],
                                    size=[200, 50],
                                    background_color=Color.RayWhite,
                                    text="Options",
                                    text_size=20,
                                    text_color=Color.Black,
                                    action=self.__option_button_action)
        self.option_button.update_text_pos()
        self.option_button.set_pos([window.screen_width // 2 - self.option_button.width // 2, 210])

        self.quit_button = Button(pos=[0, 0],
                                  size=[200, 50],
                                  background_color=Color.RayWhite,
                                  text="Quit",
                                  text_size=20,
                                  text_color=Color.Black,
                                  action=self.__quit_button_action)

        self.quit_button.update_text_pos()
        self.quit_button.set_pos([window.screen_width // 2 - self.quit_button.width // 2, 280])

    def listen_for_button_events(self, mouse_pos: tuple, window: Window) -> None:
        for ent in self.entities:
            if isinstance(ent, Button):
                possible_event = ent.on_click(mouse_pos)
                if callable(possible_event):
                    possible_event(window)


class OptionMenuFamily(Family):
    options_text_box: TextBox = None
    sounds_button: Button = None
    mm_button: Button = None

    __toggle_sound: bool = False

    def __sounds_button_action(self, window: Window):
        if self.__toggle_sound:
            self.sounds_button.text = "Sound: On"
            self.sounds_button.update_text_pos()
        else:
            self.sounds_button.text = "Sound: Off"
            self.sounds_button.update_text_pos()
        self.__toggle_sound = not self.__toggle_sound

    def __mm_button_action(self, window: Window):
        window.menu_state = MenuState.Menu

    def init_entities(self, window: Window):
        self.options_text_box = TextBox(pos=[0, 0],
                                        size=[200, 50],
                                        background_color=Color.Silver,
                                        text="Options",
                                        text_color=Color.Black,
                                        text_size=50)
        self.options_text_box.update_text_pos()
        self.options_text_box.set_pos([window.screen_width // 2 - self.options_text_box.width // 2, 20])

        self.sounds_button = Button(pos=[0, 0],
                                    size=[200, 50],
                                    background_color=Color.RayWhite,
                                    text="Sound: On",
                                    text_size=20,
                                    text_color=Color.Black,
                                    action=self.__sounds_button_action)

        self.sounds_button.update_text_pos()
        self.sounds_button.set_pos([window.screen_width // 2 - self.sounds_button.width // 2, 140])

        self.mm_button = Button(pos=[0, 0],
                                size=[200, 50],
                                background_color=Color.RayWhite,
                                text="Back To Main Menu",
                                text_size=20,
                                text_color=Color.Black,
                                action=self.__mm_button_action)

        self.mm_button.update_text_pos()
        self.mm_button.set_pos([window.screen_width // 2 - self.mm_button.width // 2, 350])

    def listen_for_button_events(self, mouse_pos: tuple, window: Window) -> None:
        for ent in self.entities:
            if isinstance(ent, Button):
                possible_event = ent.on_click(mouse_pos)
                if callable(possible_event):
                    possible_event(window)
