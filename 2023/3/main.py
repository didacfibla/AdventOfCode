# Leemos el fichero
import re

f = open("input.txt", "r")
lines = [linea.rstrip('\n') for linea in f]


def prepare():
    columns = len(lines[0])
    files = len(lines)

    # Creamos una matriz
    matrix = []
    for fila in range(0, files):
        matrix.append([])
        for column in range(0, columns):
            matrix[fila].append(lines[fila][column])

    # for elem in matrix:
    # print(elem)

    return matrix


def find_symbols(matrix):
    # print("Searching symbols...")
    symbol_index = []
    for fila in range(0, len(matrix)):
        for columna in range(0, len(matrix[fila])):
            value = matrix[fila][columna]
            if not value.isdigit() and value != ".":
                symbol_index.append((fila, columna))
    # print(symbol_index)
    return symbol_index


def find_gears(matrix):
    # print("Searching gears...")
    gear_index = []
    for fila in range(0, len(matrix)):
        for columna in range(0, len(matrix[fila])):
            value = matrix[fila][columna]
            if value == "*":
                gear_index.append((fila, columna))
    # print(gear_index)
    return gear_index


def check_adjacent(fila, columna, matrix, symbols_cord):
    filas = len(matrix)
    columnas = len(matrix[0])

    # Verificar los 8 posibles movimientos adyacentes
    movimientos = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        # Verificar si la nueva posición está dentro de los límites de la matriz
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            # Verificar si hay un simbolo en la posición adyacente
            if (nueva_fila, nueva_columna) in symbols_cord:
                return True

    # No se encontró un simbolo adyacente
    return False


def find_numbers(matrix, symbol_index) -> list:
    total = 0
    pattern = re.compile("\\d+")

    for line_number in range(0, len(matrix)):
        line = ''.join(lines[line_number])
        for match in pattern.finditer(line):
            # print(f"Checking adjacent symbol for number: {match.group()}")
            for x in range(match.start(), match.end()):
                if check_adjacent(line_number, x, matrix, symbol_index):
                    total += int(match.group())
                    # print(f"\tAdjacent!")
                    break
    return total


def check_gear_adjacent(fila, columna, matrix):
    filas = len(matrix)
    columnas = len(matrix[0])

    # Verificar los 8 posibles movimientos adyacentes
    movimientos = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        # Verificar si la nueva posición está dentro de los límites de la matriz
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            # Verificar si hay un simbolo en la posición adyacente
            if matrix[nueva_fila][nueva_columna] == '*':
                return (nueva_fila, nueva_columna)

    # No se encontró un simbolo adyacente
    return False


def calculate_gear_radio(matrix, gears_index) -> list:
    total = 0
    pattern = re.compile("\\d+")

    adjacent_gears_count = {}

    for line_number in range(0, len(matrix)):
        line = ''.join(lines[line_number])
        for match in pattern.finditer(line):
            # print(f"Checking adjacent gear for number: {match.group()}")
            for x in range(match.start(), match.end()):
                if gear_pos := check_gear_adjacent(line_number, x, matrix):
                    if gear_pos not in adjacent_gears_count.keys():
                        adjacent_gears_count[gear_pos] = set()
                        adjacent_gears_count[gear_pos].add(match.group())
                    else:
                        adjacent_gears_count[gear_pos].add(match.group())

    for gear in adjacent_gears_count.keys():
        values = adjacent_gears_count[gear]
        if len(values) == 2:
            val1, val2 = list(values)
            total += (int(val1) * int(val2))

    return total


def part1(matrix):
    # Find symbol cord
    symbol_index = find_symbols(matrix)

    # Get all the numbers
    total = find_numbers(matrix, symbol_index)
    print(total)


def part2(matrix):
    gears_index = find_gears(matrix)
    gear_radio = calculate_gear_radio(matrix, gears_index)
    print(gear_radio)


if __name__ == '__main__':
    matrix = prepare()
    part1(matrix)  # Correct solution: 553825
    part2(matrix)  # Correct solution: 93994191
