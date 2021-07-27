import pygame
import os.path

from base.common import Color

from typing import Union, Callable


class TextBox(object):
    """
    TextBox class. This is my base class for GUI objects. When instantiated, it
    will draw a rectangle to the screen with some text on it. The text can be
    centered using its center_text function. A custom text position within the
    TextBox can also be set.
    """

    def __init__(self,
                 pos: list,
                 size: list,
                 background_color: Union[Color, tuple, list],
                 text: str = "",
                 text_pos: list = None,
                 text_size: int = 20,
                 text_color: Union[Color, tuple] = Color.Black,
                 font: pygame.font.Font = None):

        self.pos = pos
        self.size = size
        self.background_color = background_color
        self.text = text
        self.text_pos = text_pos or [20, 20]
        self.text_size = text_size
        self.text_color = text_color

        self.font = font or pygame.font.Font("resource/fonts/lunchds.ttf", text_size)

        self.surf = pygame.Surface(self.size)
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        self.rect = self.surf.get_rect(topleft=self.pos)

        self.__draw_to_self(self.font)
        self.__center_text()

    def draw_to(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.surf, self.rect)

    def set_pos(self, new_pos: list = None):
        if new_pos is None:
            new_pos = self.pos
        self.rect.x = new_pos[0]
        self.rect.y = new_pos[1]

    def set_font(self, font_filename: str = ""):
        if font_filename == "":
            return
        font_path = os.path.join("resource/fonts/", font_filename)
        self.font = pygame.font.Font(font_path, self.text_size)

    def update_text_pos(self, new_pos: list = None) -> None:
        if new_pos is None:
            new_pos = self.text_pos
        self.surf.fill([0, 0, 0, 0])
        self.text_pos = new_pos
        self.surf.fill(self.background_color)
        self.surf.blit(self.text_render, self.text_pos)

    def __draw_to_self(self, font: pygame.font.Font) -> None:
        self.surf.fill(self.background_color)
        self.text_render = font.render(self.text, False, self.text_color)
        self.surf.blit(self.text_render, self.text_pos)

    def __center_text(self) -> None:
        self.surf.fill([0, 0, 0, 0])
        self.text_pos = [(self.size[0] // 2) - self.text_render.get_rect().centerx,
                         (self.size[1] // 2) - self.text_render.get_rect().centery]
        self.surf.fill(self.background_color)
        self.surf.blit(self.text_render, self.text_pos)


class Button(TextBox):
    """
    This is my Button class. It is another GUI object that inherits from the
    TextBox class. The button class contains all the same attributes as the
    TextBox class, but with one added function: on_click. When clicked, it return
    the menu_state the button was intended to change.
    """

    def __init__(self,
                 pos: list,
                 size: list,
                 background_color: Union[Color, tuple, list],
                 text: str = "",
                 text_size: int = 20,
                 text_pos: list = None,
                 text_color: tuple = Color.Black,
                 font: pygame.font.Font = None,
                 action: object = None):
        super().__init__(pos, size, background_color, text, text_pos, text_size, text_color, font)
        self.action = action

    def on_click(self, mouse_pos: tuple) -> Union[None, Callable]:
        if (self.rect.left < mouse_pos[0] < self.rect.right and
                self.rect.top < mouse_pos[1] < self.rect.bottom):
            if isinstance(self.action, Callable):
                return self.action
