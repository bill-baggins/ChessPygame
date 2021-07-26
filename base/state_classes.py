

class MenuState:
    (Menu,
     Options,
     Game,
     Quit) = range(0, 4)


class GameState:
    (Active,
     GameOver,
     Paused) = range(0, 3)