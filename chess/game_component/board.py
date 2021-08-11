from typing import Union, Tuple, List

import pygame

from base.common import Color
from chess.chess_exception import ChessException

from chess.user_option import USER_OPTION

from chess.game_component.pieces import (
    ChessPiece, Empty, Pawn, Rook, Knight, Bishop, Queen, King
)

from chess.game_component.id import EntityID


class ChessBoard:
    def __init__(self,
                 screen_width: int,
                 screen_height: int,
                 first_square_color: Union[tuple, Color],
                 second_square_color: Union[tuple, Color]):

        self._screen_width_ref = screen_width
        self._screen_height_ref = screen_height

        self.arr_width = 8
        self.arr_height = 8

        self.first_square_color = first_square_color
        self.second_square_color = second_square_color

        self.arr: List[List[ChessPiece]] = [
            [Empty(x, y) for x in range(self.arr_width)] for y in range(self.arr_height)
        ]

        self.arr[0][self.arr_width - 1] = \
            King(0,
                 len(self.arr[0]) - 1,
                 ent_id=EntityID.KingP1,
                 texture=EntityID.KingP1[1],
                 empty=False)

        self.arr[0][0] = \
            King(x=0,
                 y=len(self.arr[0]) - 1,
                 ent_id=EntityID.KingP2,
                 texture=EntityID.KingP2[1],
                 empty=False)

        self.grid_square_width = USER_OPTION.get("grid_square_width")
        self.grid_square_height = USER_OPTION.get("grid_square_height")

        self.grid_surface = pygame.Surface([self.grid_square_width * self.arr_width,
                                            self.grid_square_height * self.arr_height]).convert()
        self.__create_checkered_grid_surf()

        self.grid_surface_width = self.grid_surface.get_width()
        self.grid_surface_height = self.grid_surface.get_height()

        self.x = (screen_width / 2) - (self.grid_surface_width / 2)
        self.y = (screen_height / 2) - (self.grid_surface_height / 2)

    def update(self):
        pass

    def get_input(self, clicked_position: Tuple[int, int]):
        mx, my = clicked_position
        if (mx < self.x or mx > self.x + self.grid_surface_width) or \
            (my < self.y or my > self.y + self.grid_surface_height):
            print("bad coords!")
            return

        rx = int((mx - self.x) // self.grid_square_width)
        ry = abs(int((my - self.y) // self.grid_square_height) - 7)

        print(f"Rel X: {rx}, Rel Y: {ry}")
        print(f"Chess Position: {chr(ord('a')+rx)}{ry+1}")

        if rx < self.arr_width and ry < self.arr_height:
            piece = self.arr[rx][ry]
            if piece.ent_id != EntityID.Empty:
                piece.move(clicked_position)

    def draw_to(self, screen: pygame.Surface):
        if self.arr is None:
            raise ChessException("Error: The grid array is empty!")

        for x in range(len(self.arr)):
            for y in range(len(self.arr[x])):
                piece = self.arr[x][y]
                if piece.ent_id[0] != 0:
                    self.grid_surface.blit(piece.texture, [x * self.grid_square_width,
                                                           y * self.grid_square_height])

        screen.blit(self.grid_surface, [self.x, self.y])

    def __draw_rect_on_grid_surf(self, x: int, y: int, color: Color):
        pygame.draw.rect(self.grid_surface,
                         color,
                         pygame.Rect(x * self.grid_square_width,
                                     y * self.grid_square_height,
                                     self.grid_square_width,
                                     self.grid_square_height))

    def __create_checkered_grid_surf(self):
        for x in range(self.arr_width):
            for y in range(self.arr_height):
                if (x + y) % 2 == 0:
                    self.__draw_rect_on_grid_surf(x, y, self.second_square_color)
                else:
                    self.__draw_rect_on_grid_surf(x, y, self.first_square_color)