import pygame
from chess.chess_exception import ChessException
from chess.user_option import USER_OPTION


class __ChessTexture:
    def __init__(self):
        self.chess_set = []
        self.image_size = 128
        self.atlas = pygame.image.load("resource/images/chess_atlas.png").convert()
        for y in range(0, self.atlas.get_height() // self.image_size):
            lst = []
            for x in range(0, self.atlas.get_width() // self.image_size):
                rect = pygame.Rect(x * self.image_size,
                                   y * self.image_size,
                                   self.image_size,
                                   self.image_size)

                subsurface = self.atlas.subsurface(rect)
                if subsurface is None:
                    raise ChessException("Unable to get subsurface from atlas.")
                subsurface = subsurface.convert()
                subsurface = pygame.transform.scale(subsurface, [USER_OPTION["grid_square_width"],
                                                                 USER_OPTION["grid_square_height"]])
                subsurface.set_colorkey([0, 0, 0])
                lst.append(subsurface)

            self.chess_set.append(lst)


chess_texture = __ChessTexture()
