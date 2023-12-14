f = open("input", "r")
lines = [linea.rstrip('\n') for linea in f]

resultado_parte1 = 0
resultado_parte2 = 0


# part 1: right side
def extrapolar_derecha(enunciado: list[int]) -> list[int]:
    enunciado = line.split()

    line_actual = []
    for elem in enunciado: line_actual.append(int(elem))

    solution = [line_actual]

    while not all(elemento == 0 for elemento in line_actual):
        nueva_linea = []

        for i in range(1, len(line_actual)):
            diferencia = line_actual[i] - line_actual[i - 1]
            nueva_linea.append(diferencia)

        line_actual = nueva_linea
        solution.append(line_actual)

    return solution


def sumar_extrapolados(solution: list[int]) -> int:
    extra_values = []
    solution[-1].append(0)

    for i in range(len(solution) - 1, 0, -1):
        # print(f"\t {solution[i][-1]} - {solution[i - 1][-1]} -> {solution[i][-1] + solution[i - 1][-1]}")
        value = solution[i][-1] + solution[i - 1][-1]
        solution[i - 1].append(value)

    extra_values.append(solution[0][-1])
    return sum(extra_values)


# part 2: left side
def extrapolar_izquierda(enunciado: list[int]) -> list[int]:
    enunciado = line.split()

    line_actual = []
    for elem in enunciado: line_actual.append(int(elem))

    solution = [line_actual]

    while not all(elemento == 0 for elemento in line_actual):
        nueva_linea = []

        for i in range(len(line_actual) - 1, 0, -1):
            diferencia = line_actual[i] - line_actual[i - 1]
            nueva_linea.insert(0, diferencia)

        line_actual = nueva_linea
        solution.append(line_actual)

    return solution


def restart_extrapolados(solution: list[int]) -> int:
    extra_values = []
    solution[-1].insert(0, 0)

    for i in range(len(solution) - 1, 0, -1):
        # print(f"\t {solution[i][-1]} - {solution[i - 1][-1]} -> {solution[i][-1] + solution[i - 1][-1]}")
        value = solution[i - 1][0] - solution[i][0]
        solution[i - 1].insert(0, value)

    extra_values.append(solution[0][0])
    return sum(extra_values)


for line in lines:
    solution_part1 = extrapolar_derecha(line)
    resultado_parte1 += sumar_extrapolados(solution_part1)

    solution_part2 = extrapolar_izquierda(lines)
    resultado_parte2 += restart_extrapolados(solution_part2)

print(resultado_parte1)
print(resultado_parte2)
