import pygame
import pygame.draw

from pygame.math import Vector2

from dataclasses import dataclass
from enum import Enum

from base.common import Color


class ChessException(Exception):
    def __init__(self, *args):
        super().__init__(args)


class EntityID:
    Empty = 0
    Pawn = 1
    Rook = 2
    Knight = 3
    Bishop = 4
    Queen = 5
    King = 6


@dataclass
class ChessPiece:
    texture: pygame.Surface
    pos: Vector2
    legal_moves: 'list[EntityID]'

    def move(self, clicked_position: Vector2):
        """
        Attempts to move the chess piece to the specified Vector2 location on
        the grid.

        If the specified location is outside the bounds of the grid, then the player
        cannot move their chess piece there.

        The player also cannot move their piece to a area where another piece is
        (as a pawn) or where they will be put in check (as the king)

        :param clicked_position: The position the user has clicked on the grid.
                                 This position needs to be truncated to a grid 
                                 coordinate, so that even if the user clicks an
                                 area that is near the edge of the window, it
                                 will not truncate the coordinate to outside of
                                 the grid array's bounds.
        :return:
        returns None
        """

    def draw_to(self, board: pygame.Surface):
        """
        Draws the chess piece to the board. Each chess piece should be the size
        of a grid square, and their drawn position is determined by its position
        on the grid.

        :param screen: The chess board, where the piece will be drawn.
        :return:
        """

    def show_legal_moves(self):
        """
        Loops through the list of legal moves and highlights the surfaces present
        at each location on the grid. If one of the legal moves is outside of the
        grid, then it will not show it as a place to move to.

        These highlighted areas on each location of the grid will appear after
        a piece gets clicked on by the user.

        :return: None.
        None
        """


class Grid:
    def __init__(self, 
                 screen_width: int, 
                 screen_height: int):

        self.arr_width = 8
        self.arr_height = 8

        self.arr = [
            [EntityID.Empty for _ in range(self.arr_width)] for _ in range(self.arr_height)
        ]
        self.grid_square_width = self.arr_width * 5
        self.grid_square_height = self.arr_height * 5

        self.grid_surface = pygame.Surface([self.grid_square_width * self.arr_width, 
                                            self.grid_square_height * self.arr_height]).convert()
        self.__create_checkered_grid_surf()

        self.grid_surface_width = self.grid_surface.get_width()
        self.grid_surface_height = self.grid_surface.get_height()

        self.x = (screen_width / 2) - (self.grid_surface_width / 2)
        self.y = (screen_height / 2) - (self.grid_surface_height / 2)

    def draw_to(self, screen: pygame.Surface):
        if self.arr is None:
            raise ChessException("Error: The grid array is empty!")
        screen.blit(self.grid_surface, [self.x, self.y])

    def __draw_rect_on_grid_surf(self, x: int, y: int, color: Color):
        pygame.draw.rect(self.grid_surface, 
                         color,
                         pygame.Rect(x*self.grid_square_width,
                                     y*self.grid_square_height,
                                     self.grid_square_width,
                                     self.grid_square_height))
    
    def __create_checkered_grid_surf(self):
        for x in range(self.arr_width):
            for y in range(self.arr_height):
                if (x + y) % 2 == 0:
                    self.__draw_rect_on_grid_surf(x, y, Color.Coffee)
                else:
                    self.__draw_rect_on_grid_surf(x, y, Color.White)


class Pawn(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):
        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        super().move(clicked_position)
