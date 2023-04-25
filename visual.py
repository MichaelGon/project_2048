import pygame
import sys


def draw_intro(game):
    img2048 = pygame.image.load('img_2048.png')

    font = pygame.font.SysFont("freesansbold.ttf", 55)
    text_welcome = font.render("Welcome!", True, 'white')
    name = 'Введите имя'
    found_name = False

    while not found_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 0 and len(name) < 8:
                        game.USERNAME = name
                        found_name = True
                        break

        game.screen.fill('black')
        text_name = font.render(name, True, 'white')
        rect_name = text_name.get_rect()
        rect_name.center = game.screen.get_rect().center
        game.screen.blit(pygame.transform.scale(img2048, [150, 150]), [15, 15])
        game.screen.blit(text_welcome, [200, 70])
        game.screen.blit(text_name, rect_name)
        pygame.display.update()
    game.screen.fill('black')


def draw_top_gamers(game):
    font_top = pygame.font.SysFont("simsun", 30)
    font_gamer = pygame.font.SysFont('arial', 24)
    text_head = font_top.render("Best tries:", True, 'black')
    game.screen.blit(text_head, [220, 400])

    for index, elem in enumerate(game.REZ):
        name, score = elem
        s = f"{index + 1}. {name} - {score}"
        text_gamer = font_gamer.render(s, True, 'black')
        game.screen.blit(text_gamer, [220, 400 + (index + 1) * 25])


def draw_over(game):
    result = game.score
    img2048 = pygame.image.load('img_2048.png')

    font = pygame.font.SysFont("freesansbold.ttf", 55)
    font1 = pygame.font.SysFont("freesansbold.ttf", 45)
    text_over = font.render("Game Over!", True, 'red')
    text_score = font1.render(f"Your Result: {result}", True, 'white')
    text_restart = font1.render("Press Enter to Restart", True, 'white')

    game.screen.fill('black')
    game.screen.blit(text_over, [170, 70])
    game.screen.blit(text_score, [10, 230])
    game.screen.blit(text_restart, [10, 270])
    game.screen.blit(pygame.transform.scale(img2048, [150, 150]), [15, 15])
    pygame.display.update()


def draw_board(game):
    pygame.draw.rect(game.screen, game.colors['bg'], [0, 0, 400, 400], 0, 10)
    score_text = game.font.render(f'Score: {game.score}', True, 'red')
    high_score_text = game.font.render(f'High Score: {game.high_score}', True, 'green')
    game.screen.blit(score_text, (7, 410))
    game.screen.blit(high_score_text, (7, 450))

    draw_top_gamers(game)

    pass


def draw_pieces(game):
    arr = game.board_values

    for i in range(4):
        for j in range(4):
            value = arr[i][j]

            if value > 8:
                value_color = game.colors['light text']
            else:
                value_color = game.colors['dark text']

            if value <= 2048:
                color = game.colors[value]
            else:
                color = game.colors['other']

            pygame.draw.rect(game.screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)

            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                game.screen.blit(value_text, text_rect)