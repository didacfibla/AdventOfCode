def move(row: int, col: int, direction: str):
    return row, col, direction


def part1(filename):
    matrix = [list(line.rstrip('\n')) for line in open(filename, "r")]

    for elem in matrix:
        print(elem)

    pending_mov = [(0, 0, "r")]

    while len(pending_mov) > 0:
        actual_position = pending_mov.pop(0)
        new_position = move(row=actual_position[0], col=actual_position[1], direction=actual_position[2])
        pending_mov.append(new_position)


if __name__ == "__main__":
    part1("example")
