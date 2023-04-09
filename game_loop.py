from func import is_any, make_turn, new_pieces
import pygame
import sqlite3
from visual import draw_over, draw_board, draw_pieces


def loop(game):
    is_game = True

    while is_game:
        game.timer.tick(game.fps)
        game.screen.fill('gray')
        draw_board(game)
        draw_pieces(game)

        if game.som_new or game.initer < 2:
            game.board_values, game.game_over = new_pieces(game)
            game.som_new = False
            game.initer += 1

        if game.direction != '':
            game.board_values = make_turn(game)
            game.direction = ''
            game.som_new = True

        if game.game_over and not is_any(game):
            draw_over(game)
            if game.high_score > game.init_high:
                file = open('high_score', 'w')
                file.write(f'{game.high_score}')
                file.close()
                game.init_high = game.high_score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    game.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    game.direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    game.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    game.direction = 'RIGHT'

                if game.game_over and not is_any(game):
                    ans = list()
                    helper = (game.USERNAME, game.score)
                    ans.append(helper)

                    with sqlite3.connect("2048.sqlite") as bd:
                        cur = bd.cursor()

                        cur.execute("""INSERT INTO RECORDS VALUES (?, ?)""", ans[0])

                        cur.close()
                    if event.key == pygame.K_RETURN:
                        game.board_values = [[0 for _ in range(4)] for _ in range(4)]
                        game.som_new = True
                        game.initer = 0
                        game.score = 0
                        game.direction = ''
                        game.game_over = False

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

                        game.REZ = cur.fetchall()

        if game.score > game.high_score:
            game.high_score = game.score

        pygame.display.flip()
