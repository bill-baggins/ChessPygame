# chess_entities.py: Contains definitions for each of the chess pieces, the
# chess board, and the players.

# TODO: Add player logic. Players will be able to keep track of their pieces
#       through a dictionary.

from dataclasses import dataclass
from typing import Union

import pygame
import pygame.draw
from pygame.math import *

from base.common import Color
from chess.chess_exception import ChessException
from chess.chess_texture import chess_texture as ct

from chess.user_option import USER_OPTION


class Vector2(Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)

    def as_list(self) -> 'list[float]':
        return [self.x, self.y]


p1 = USER_OPTION.get("player_one_index")
p2 = USER_OPTION.get("player_two_index")


class EntityID:
    global p1, p2

    Empty = 0, pygame.Surface([0, 0])
    PawnP1 = 1, ct.chess_set[p1][0]
    KnightP1 = 2, ct.chess_set[p1][1]
    BishopP1 = 3, ct.chess_set[p1][2]
    RookP1 = 4, ct.chess_set[p1][3]
    QueenP1 = 5, ct.chess_set[p1][4]
    KingP1 = 6, ct.chess_set[p1][5]
    PawnP2 = 7, ct.chess_set[p2][0]
    KnightP2 = 8, ct.chess_set[p2][1]
    BishopP2 = 9, ct.chess_set[p2][2]
    RookP2 = 10, ct.chess_set[p2][3]
    QueenP2 = 11, ct.chess_set[p2][4]
    KingP2 = 12, ct.chess_set[p2][5]


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
        raise NotImplementedError

    def draw_to(self, board: pygame.Surface):
        """
        Draws the chess piece to the board. Each chess piece should be the size
        of a grid square, and their drawn position is determined by its position
        on the grid.
        Do not override this function.

        :param board: The chess board, where the piece will be drawn.
        :return:
        """
        board.blit(self.texture, self.pos.as_list())

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
        raise NotImplementedError

    def get_legal_moves(self):
        """
        Custom defined function for each piece class that governs how and where
        chess pieces are allowed to move within the grid.

        :return:
        """
        raise NotImplementedError


class Grid:
    def __init__(self, 
                 screen_width: int, 
                 screen_height: int,
                 first_square_color: Union[tuple, Color],
                 second_square_color: Union[tuple, Color]):

        self.arr_width = 8
        self.arr_height = 8
        self.first_square_color = first_square_color
        self.second_square_color = second_square_color

        self.arr = [
            [EntityID.KingP1 for _ in range(self.arr_width)] for _ in range(self.arr_height)
        ]
        self.grid_square_width = USER_OPTION["grid_square_width"]
        self.grid_square_height = USER_OPTION["grid_square_height"]

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

        for x in range(len(self.arr)):
            for y in range(len(self.arr[x])):
                piece = self.arr[x][y]
                if piece[0] != 0:
                    self.grid_surface.blit(piece[1], [x * self.grid_square_width,
                                                      y * self.grid_square_height])

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
                    self.__draw_rect_on_grid_surf(x, y, self.second_square_color)
                else:
                    self.__draw_rect_on_grid_surf(x, y, self.first_square_color)


class Pawn(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):
        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Rook(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):

        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Knight(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):

        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Bishop(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):

        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Queen(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):

        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class King(ChessPiece):
    def __init__(self,
                 texture: pygame.Surface,
                 pos: Vector2,
                 legal_moves: 'list[Vector2]'):

        super().__init__(texture, pos, legal_moves)

    def move(self, clicked_position: Vector2):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass
