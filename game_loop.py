from func import is_any, make_turn, new_pieces
from init import Globals
import pygame
import sqlite3
from visual import draw_over, draw_board, draw_pieces


class Loop(object):
    is_game = True
    game = Globals()

    def __init__(self, elem):
        self.game = elem

    def upload(self):
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

            self.game.REZ = cur.fetchall()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.game.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    self.game.direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.game.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    self.game.direction = 'RIGHT'

                if self.game.game_over and not is_any(self.game):
                    ans = list()
                    helper = (self.game.USERNAME, self.game.score)
                    ans.append(helper)

                    with sqlite3.connect("2048.sqlite") as bd:
                        cur = bd.cursor()

                        cur.execute("""INSERT INTO RECORDS VALUES (?, ?)""", ans[0])

                        cur.close()
                    if event.key == pygame.K_RETURN:
                        self.game.board_values = [[0 for _ in range(4)] for _ in range(4)]
                        self.game.som_new = True
                        self.game.initer = 0
                        self.game.score = 0
                        self.game.direction = ''
                        self.game.game_over = False

                    self.upload()

    def loop(self):
        while self.is_game:
            self.game.timer.tick(self.game.fps)
            self.game.screen.fill('gray')
            draw_board(self.game)
            draw_pieces(self.game)

            if self.game.som_new or self.game.initer < 2:
                self.game.board_values, self.game.game_over = new_pieces(self.game)
                self.game.som_new = False
                self.game.initer += 1

            if self.game.direction != '':
                self.game.board_values = make_turn(self.game)
                self.game.direction = ''
                self.game.som_new = True

            if self.game.game_over and not is_any(self.game):
                draw_over(self.game)
                if self.game.high_score > self.game.init_high:
                    file = open('high_score', 'w')
                    file.write(f'{self.game.high_score}')
                    file.close()
                    self.game.init_high = self.game.high_score

            self.event()

            if self.game.score > self.game.high_score:
                self.game.high_score = self.game.score

            pygame.display.flip()
