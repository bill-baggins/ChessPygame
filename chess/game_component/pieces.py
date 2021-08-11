from dataclasses import dataclass
from typing import Union, Tuple, List

import pygame

from chess.game_component.id import EntityIDType, EntityID


@dataclass
class ChessPiece:
    ent_id: EntityIDType
    texture: pygame.Surface
    pos: Union[List[int], Tuple[int, int]]

    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):

        if empty:
            self.ent_id = EntityID.Empty
            self.texture = self.ent_id[1]
            self.pos = (x, y)
            self.legal_moves = []
        else:
            self.ent_id = ent_id
            self.texture = texture
            self.pos = (x, y)
            self.legal_moves = []

    def change_id_to(self, new_id: EntityIDType):
        self.ent_id = new_id
        self.texture = new_id[1]

    def move(self, clicked_position: Tuple[int, int]):
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
        raise NotImplementedError("This class method must be overridden.")

    def draw_to(self, board: pygame.Surface):
        """
        Draws the chess piece to the board. Each chess piece should be the size
        of a grid square, and their drawn position is determined by its position
        on the grid.
        Do not override this function.

        :param board: The chess board, where the piece will be drawn.
        :return:
        """
        board.blit(self.texture, self.pos)

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
        raise NotImplementedError("This class method must be overridden.")

    def get_legal_moves(self):
        """
        Custom defined function for each piece class that governs how and where
        chess pieces are allowed to move within the grid.

        :return:
        """
        raise NotImplementedError("This class method must be overridden.")

    def __repr__(self):
        return {
            EntityID.KingP1: "King",
            EntityID.KingP2: "King",
            EntityID.QueenP1: "Queen",
            EntityID.QueenP2: "Queen",
            EntityID.RookP2: "Rook",
            EntityID.RookP1: "Rook",
            EntityID.KnightP1: "Knight",
            EntityID.KnightP2: "Knight",
            EntityID.BishopP1: "Bishop",
            EntityID.BishopP2: "Bishop",
            EntityID.PawnP1: "Pawn",
            EntityID.PawnP2: "Pawn",
        }.get(self.ent_id, EntityID.Empty)


class Empty(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):
        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Pawn(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):

        super().__init__(x, y, ent_id, texture, empty)
        self.on_first_move = True
        self.legal_moves = []

    def move(self, clicked_position: Tuple[int, int]):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Rook(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):

        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Knight(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):
        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Bishop(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):
        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        pass

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class Queen(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):

        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        print("Hello")

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass


class King(ChessPiece):
    def __init__(self,
                 x: int,
                 y: int,
                 ent_id: EntityIDType = None,
                 texture: pygame.Surface = None,
                 empty: bool = True):
        super().__init__(x, y, ent_id, texture, empty)

    def move(self, clicked_position: Tuple[int, int]):
        print("I got called!")

    def show_legal_moves(self):
        pass

    def get_legal_moves(self):
        pass
