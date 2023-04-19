from game_loop import Loop
from init import Globals
import pygame
from visual import draw_intro


pygame.init()

consts = Globals()
draw_intro(consts)

game = Loop(consts)
game.loop()

pygame.quit()
