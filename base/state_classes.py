

class MenuState:
    (Menu,
     Options,
     Game,
     Paused,
     Quit) = range(0, 5)


class GameState:
    (Active,
     GameOver,
     Paused) = range(0, 3)