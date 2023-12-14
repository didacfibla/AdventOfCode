f = open("example", "r")
lines = [linea.rstrip('\n') for linea in f]

enunciado = lines[0].split()

line_actual = []
for elem in enunciado: line_actual.append(int(elem))

solution = [line_actual]

while not all(elemento == 0 for elemento in line_actual):
    nueva_linea = []

    print("Linea actual: ", line_actual)

    for i in range(1, len(line_actual)):
        diferencia = line_actual[i] - line_actual[i - 1]
        print(f"i: {i} -> {line_actual[i]} - {line_actual[i - 1]} = {diferencia}")
        nueva_linea.append(diferencia)

    line_actual = nueva_linea
    solution.append(line_actual)

print("______________")
for elem in solution:
    print(elem)
