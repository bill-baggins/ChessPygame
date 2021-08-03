from base.settings import SCREEN_SETTING

USER_OPTION = {
    "player_one_index": 2,
    "player_two_index": 3,
    "grid_square_width": int(SCREEN_SETTING["size"][0] / (16/8) / 8),
    "grid_square_height": int(SCREEN_SETTING["size"][1] / (10/8) / 8)
}
