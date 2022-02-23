import random

from structure import Structure


if __name__ == '__main__':
    game_field = [[random.randint(1, 3) for x in range(15)] for y in range(10)]
    for y in range(10):
        for x in range(15):
            if game_field[y][x] == 1:
                game_field[y][x] = 'R'
            if game_field[y][x] == 2:
                game_field[y][x] = 'G'
            if game_field[y][x] == 3:
                game_field[y][x] = 'B'
    structure = Structure(game_field)

    score = 0
    move_count = 0
    is_continuing = True

    while is_continuing:
        structure.show_colors()
        print('type y')
        y = int(input())
        print('type x')
        x = int(input())
        result = structure.remove(y, x)
        if result[0] > -1:
            move_count += 1
            balls_count = result[0]
            color = result[1]
            current_score = (balls_count - 2) ** 2
            score += current_score
            print(f'Move {move_count} at ({x}, {y}): removed {balls_count} balls of color {color}, got {current_score} points')
        if not structure.is_valid_cluster(structure.get_biggest_cluster()):
            structure.show_colors()
            remaining = structure.get_remaining_balls()
            if remaining == 0:
                score += 1000
            is_continuing = False
            print(f'Game finished with score {score}')
            input()
