import pygame

from typing import Tuple
from chess.game_component.piece_texture import chess_texture as ct
from chess.user_option import USER_OPTION

p1 = USER_OPTION.get("player_one_index")
p2 = USER_OPTION.get("player_two_index")

EntityIDType = Tuple[int, pygame.Surface]
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
