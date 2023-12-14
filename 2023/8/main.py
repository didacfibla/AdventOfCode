import sys
from collections import Counter

f = open("input.txt", "r")
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
    return 'Z' in solution


def factorizar_primos(numero):
    factores_primos = Counter()
    divisor = 2
    while divisor * divisor <= numero:
        while (numero % divisor) == 0:
            factores_primos[divisor] += 1
            numero //= divisor
        divisor += 1
    if numero > 1:
        factores_primos[numero] += 1
    return factores_primos


def mcm(lista: list[int]) -> int:
    factores_comunes = Counter()

    for numero in lista:
        factores_numero = factorizar_primos(numero)
        factores_comunes = factores_comunes | factores_numero

    mcm = 1
    for factor, exponente in factores_comunes.items():
        mcm *= factor ** exponente

    return mcm


def part2():
    steps = 0

    # Get all nodes with an 'A' to start that path
    start_positions = []

    for key in puzzle:
        if 'A' in key:
            start_positions.append(key)

    steps_to_solve = [0] * len(start_positions)

    for start_position in start_positions:

        actual = start_position

        while not check_solution(actual):
            # print(f"Estamos en {actual}")
            if len(movements) > 0:
                movement = movements.pop(0)

                if len(movements) == 0:
                    for movement in movements_:
                        movements.append(movement)

            actual = get_next(actual, movement)

            # print(f"Nos vamos a {movement} -> {actual}")
            steps_to_solve[start_positions.index(start_position)] += 1

            # print("....")

    print(mcm(steps_to_solve))


if __name__ == '__main__':
    # part1()
    part2()
