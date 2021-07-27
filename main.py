# main.py: Application entry point.
def main_loop():
    while window.running:
        if window.menu_state == MenuState.Menu:
            menu_loop()
        elif window.menu_state == MenuState.Game:
            game_loop()
        elif window.menu_state == MenuState.Quit:
            window.running = False
            break


def menu_loop():
    global window
    menu_ent = menu.MenuSystem()
    menu.initialize(window, menu_ent)
    while window.menu_state == MenuState.Menu or \
            window.menu_state == MenuState.Options:

        menu.event_loop(window, menu_ent)
        menu.update(window, menu_ent)
        menu.draw(window, menu_ent)
        window.ms = window.clock.tick(SCREEN_SETTING.get("fps"))


def game_loop():
    global window
    game_ent = game.GameSystem()
    # Edit the window and game_ent objects
    game.initialize(window, game_ent)
    while window.menu_state == MenuState.Game:
        game.event_loop(window, game_ent)
        game.update(window, game_ent)
        game.draw(window, game_ent)
        window.ms = window.clock.tick(SCREEN_SETTING.get("fps"))


if __name__ == "__main__":
    import pygame
    pygame.init()
    pygame.font.init()

    from pygame.constants import *

    from base.window import Window, MenuState
    from base.settings import SCREEN_SETTING

    import chess.game as game
    import chess.menu as menu

    pygame.display.set_mode(SCREEN_SETTING["size"], FULLSCREEN if SCREEN_SETTING["fullscreen"] else 0)
    pygame.display.set_caption(SCREEN_SETTING["title"])

    window = Window()
    
    main_loop()

    pygame.quit()
