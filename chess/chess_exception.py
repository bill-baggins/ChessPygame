# chess_exception.py: The most useless file ever conceived by any programmer ever.

class ChessException(Exception):
    def __init__(self, *args):
        super().__init__(args)