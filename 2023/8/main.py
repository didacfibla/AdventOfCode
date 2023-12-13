import sys

f = open("index.txt", "r")
lines = [linea.rstrip('\n') for linea in f]

movements_ = lines[0]
movements = []

for movement in movements_:
    movements.append(movement)

puzzle = {}
for i in range(2, len(lines)):
    content = lines[i].split()
    puzzle[content[0]] = (content[2][1:-1], content[3][:-1])


def part1():
    actual_position = 'AAA'
    steps = 0

    while actual_position != 'ZZZ':
        if len(movements) > 0:
            movement = movements.pop(0)

            if len(movements) == 0:
                for movement in movements_:
                    movements.append(movement)

            if movement == 'L':
                movement_index = 0
            else:
                movement_index = 1

            # print(f"{actual_position} -> Move to {movement} -> {puzzle[actual_position]} -> {puzzle[actual_position][movement_index]}")
            actual_position = puzzle[actual_position][movement_index]
            steps += 1

    print(steps)


def get_next(actual_position, movement):
    return puzzle[actual_position][0 if movement == 'L' else 1]


def check_solution(solution):
    return all('Z' in s for s in solution)


def part2():
    steps = 0

    # Get all nodes with an 'A' to start that path
    start_positions = []
    for key in puzzle:
        if 'A' in key:
            start_positions.append(key)

    actual_position = start_positions
    print(actual_position)

    while not check_solution(actual_position):
        if len(movements) > 0:
            movement = movements.pop(0)

            if len(movements) == 0:
                for movement in movements_:
                    movements.append(movement)

            next_path = []

            for path in actual_position:
                next_path.append(get_next(path, movement))

            print(next_path)

            actual_position = next_path
            steps += 1
            print(steps)

    print(steps)


if __name__ == '__main__':
    # part1()
    part2()
