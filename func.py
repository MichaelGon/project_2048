import random


def is_any(game):
    arr = game.board_values
    help = [[False for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            helper = 0

            if i > 0:
                for k in range(i):
                    if arr[k][j] == 0:
                        helper += 1

                if arr[i - helper - 1][j] == arr[i - helper][j] and not help[i - helper - 1][j] and not help[i - helper][j]:
                    return True

    for i in range(3):
        for j in range(4):
            helper = 0

            for k in range(i + 1):
                if arr[3 - k][j] == 0:
                    helper += 1

            if 3 - i + helper <= 3:
                if arr[2 - i + helper][j] == arr[3 - i + helper][j] and not help[3 - i + helper][j] and not help[2 - i + helper][j]:
                    return True

    for i in range(4):
        for j in range(4):
            helper = 0

            for k in range(j):
                if arr[i][k] == 0:
                    helper += 1

            if j > 0 and arr[i][j - helper] == arr[i][j - helper - 1] and not help[i][j - helper - 1] and not help[i][j - helper]:
                return True

    for i in range(4):
        for j in range(3, -1, -1):
            helper = 0

            for k in range(3, j, -1):
                if arr[i][k] == 0:
                    helper += 1

            if 1 + j + helper <= 3:
                if arr[i][j + helper] == arr[i][1 + j + helper] and not help[i][j + helper] and not help[i][1 + j + helper]:
                    return True
    return False


def make_turn(game):
    arr = game.board_values
    combined = [[False for _ in range(4)] for _ in range(4)]

    if game.direction == 'UP':
        for i in range(4):
            for j in range(4):
                helper = 0

                if i > 0:
                    for k in range(i):
                        if arr[k][j] == 0:
                            helper += 1
                    if helper > 0:
                        arr[i - helper][j] = arr[i][j]
                        arr[i][j] = 0

                    if arr[i - helper - 1][j] == arr[i - helper][j] and not combined[i - helper - 1][j] and not combined[i - helper][j]:
                        arr[i - helper - 1][j] *= 2
                        game.score += arr[i - helper - 1][j]
                        arr[i - helper][j] = 0
                        combined[i - helper - 1][j] = True
    elif game.direction == 'DOWN':
        for i in range(3):
            for j in range(4):
                helper = 0

                for k in range(i + 1):
                    if arr[3 - k][j] == 0:
                        helper += 1
                if helper > 0:
                    arr[2 - i + helper][j] = arr[2 - i][j]
                    arr[2 - i][j] = 0

                if 3 - i + helper <= 3:
                    if arr[2 - i + helper][j] == arr[3 - i + helper][j] and not combined[3 - i + helper][j] and not combined[2 - i + helper][j]:
                        arr[3 - i + helper][j] *= 2
                        game.score += arr[3 - i + helper][j]
                        arr[2 - i + helper][j] = 0
                        combined[3 - i + helper][j] = True
    elif game.direction == 'LEFT':
        for i in range(4):
            for j in range(4):
                helper = 0

                for k in range(j):
                    if arr[i][k] == 0:
                        helper += 1
                if helper > 0:
                    arr[i][j - helper] = arr[i][j]
                    arr[i][j] = 0

                if j > 0 and arr[i][j - helper] == arr[i][j - helper - 1] and not combined[i][j - helper - 1] and not combined[i][j - helper]:
                    arr[i][j - helper - 1] *= 2
                    game.score += arr[i][j - helper - 1]
                    arr[i][j - helper] = 0
                    combined[i][j - helper - 1] = True
    elif game.direction == 'RIGHT':
        for i in range(4):
            for j in range(3, -1, -1):
                helper = 0

                for k in range(3, j, -1):
                    if arr[i][k] == 0:
                        helper += 1
                if helper > 0:
                    arr[i][j + helper] = arr[i][j]
                    arr[i][j] = 0

                if 1 + j + helper <= 3:
                    if arr[i][j + helper] == arr[i][1 + j + helper] and not combined[i][j + helper] and not combined[i][1 + j + helper]:
                        arr[i][1 + j + helper] *= 2
                        game.score += arr[i][j + helper + 1]
                        arr[i][j + helper] = 0
                        combined[i][1 + j + helper] = True
    return arr


def new_pieces(game):
    arr = game.board_values
    
    over = False
    counter = 0

    while any(0 in elem for elem in arr) and counter < 1:
        elem = random.randint(0, 3)
        col = random.randint(0, 3)

        if arr[elem][col] == 0:
            counter += 1
            if random.randint(1, 10) == 10:
                arr[elem][col] = 4
            else:
                arr[elem][col] = 2

    if counter < 1:
        over = True

    return arr, over
