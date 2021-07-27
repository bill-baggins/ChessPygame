import pygame
import os.path
from typing import Union, Callable


# Color class. Has named attributes of various colors I use often.
class Color:
    Black = 0, 0, 0, 255
    RayWhite = 235, 235, 235, 255
    White = 255, 255, 255, 255
    Gray = 124, 124, 124, 255
    Red = 200, 50, 0, 255
    Blue = 0, 100, 200, 255
    Green = 0, 255, 0, 255
    DarkGreen = 7, 75, 21, 255
    Silver = 192, 192, 192, 255
    Coffee = 111, 78, 55, 255


class GameFont:
    Small = pygame.font.Font("resource/fonts/lunchds.ttf", 20)
    Default = pygame.font.Font("resource/fonts/lunchds.ttf", 30)
    Title = pygame.font.Font("resource/fonts/lunchds.ttf", 50)
    Arrow = pygame.font.Font("resource/fonts/lunchds.ttf", 80)


class MouseButton:
    (Left,
     Middle,
     Right) = range(1, 4)
