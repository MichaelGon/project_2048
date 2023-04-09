from game_loop import loop
from init import Globals
import pygame
from visual import draw_intro


pygame.init()

game = Globals()
draw_intro(game)

loop(game)

pygame.quit()
