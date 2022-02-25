import random
from structure import Structure

if __name__ == '__main__':
    print('Input number of games')
    games_count = int(input())

    for i in range(games_count):
        print(f'Game {i+1}:')
        game_field = [[random.randint(1, 3) for x in range(15)] for y in range(10)]

        # random generation of game field
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

        while True:
            if not structure.is_valid_cluster(structure.get_biggest_cluster()):  # if no valid clusters left
                balls_remaining = structure.get_remaining_balls()
                if balls_remaining == 0:
                    score += 1000  # bonus 1000 if no balls left
                print(f'Final score: {score}, with {balls_remaining} balls remaining.\n')
                break
            axes = structure.get_cluster_axes(structure.get_biggest_cluster())
            result = structure.remove(axes[0], axes[1])

            move_count += 1
            balls_count = result[0]
            color = result[1]
            current_score = (balls_count - 2) ** 2
            score += current_score
            print(
                f'Move {move_count} at ({axes[1]}, {axes[0]}): removed {balls_count} balls of color {color}, got {current_score} points')

    input()