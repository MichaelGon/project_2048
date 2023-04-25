import pygame
import sqlite3
pygame.font.init()

WIDTH = 400
HEIGHT = 500


class Globals(object):
    REZ = list()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Game 2048")

    timer = pygame.time.Clock()
    fps = 60
    font = pygame.font.SysFont('freesansbold.ttf', 33)

    colors = {0: (204, 192, 179),
              2: (238, 228, 218),
              4: (237, 224, 200),
              8: (242, 177, 121),
              16: (245, 149, 99),
              32: (246, 124, 95),
              64: (246, 94, 59),
              128: (237, 207, 114),
              256: (237, 204, 97),
              512: (237, 208, 80),
              1024: (237, 197, 63),
              2048: (237, 194, 46),
              'light text': (249, 246, 242),
              'dark text': (119, 110, 101),
              'other': (80, 200, 120),
              'bg': (187, 173, 160)}

    board_values = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    game_over = False
    som_new = True
    initer = 0
    direction = ''
    score = 0
    file = open('high_score', 'r')
    init_high = int(file.readline())
    file.close()
    high_score = init_high

    USERNAME = None

    def __init__(self):
        with sqlite3.connect("2048.sqlite") as bd:
            cur = bd.cursor()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS RECORDS (
                name text,
                score integer
            )""")

            cur.execute("""
            SELECT name gamer, max(score) score
            FROM RECORDS
            GROUP BY name
            ORDER BY score DESC
            limit 3
            """)

            self.REZ = cur.fetchall()

            cur.close()
