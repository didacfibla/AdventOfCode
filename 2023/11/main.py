from collections import deque
from itertools import combinations


def find_expansions(universe):
    filas = len(universe)
    columnas = len(universe[0])

    filas_punto = []
    columnas_punto = []

    for i in range(filas):
        # Verificar si la fila contiene únicamente puntos
        if all(elem == '.' for elem in universe[i]):
            filas_punto.append(i)

    for j in range(columnas):
        # Verificar si la columna contiene únicamente puntos
        if all(universe[i][j] == '.' for i in range(filas)):
            columnas_punto.append(j)

    return filas_punto, columnas_punto


def expand_universe(universe, expansion_cords):
    expansion_times = 1

    cols_inserted = 0
    for col_to_exapand in expansion_cords[1]:
        for i in range(0, expansion_times):
            for row in universe:
                row.insert(col_to_exapand + cols_inserted, '.')
            cols_inserted += 1

    new_row = ['.' for _ in range(len(universe[0]))]
    rows_inserted = 0
    for row_to_exapand in expansion_cords[0]:
        for i in range(0, expansion_times):
            universe.insert(row_to_exapand + rows_inserted, new_row)
            rows_inserted += 1


def load_data(filename):
    # Load the universe
    universe = [list(line.rstrip('\n')) for line in open(filename, "r")]

    # Expand the universe
    expansion_coords = find_expansions(universe)
    expand_universe(universe, expansion_coords)

    # Locate galaxies
    galaxies = [(i, j) for i, row in enumerate(universe) for j, elem in enumerate(row) if elem == '#']

    numero_actual = 1
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                universe[i][j] = numero_actual
                numero_actual += 1

    return universe, galaxies


def generar_pares(elementos):
    pares = list(combinations(elementos, 2))
    return pares


def shortest_path(matriz, inicio, destino):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Definir movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Inicializar la cola para BFS
    cola = deque([(inicio[0], inicio[1], 0)])  # (fila, columna, distancia)

    # Marcar la posición de inicio como visitada
    visitado = set([(inicio[0], inicio[1])])

    while cola:
        fila, columna, distancia = cola.popleft()

        # Verificar si hemos llegado al destino
        if (fila, columna) == destino:
            return distancia

        # Explorar los movimientos posibles
        for movimiento in movimientos:
            nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]

            # Verificar si la nueva posición está dentro de la matriz
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                # Marcar la nueva posición como visitada y agregar a la cola
                nueva_posicion = (nueva_fila, nueva_columna)
                if nueva_posicion not in visitado:
                    visitado.add(nueva_posicion)
                    cola.append((nueva_fila, nueva_columna, distancia + 1))

    # Si no se encuentra un camino, devolver -1
    return -1


if __name__ == "__main__":
    u, g = load_data("input")

    pares = generar_pares(g)
    input(f"Hay {len(pares)} pares, presiona una tecla para empezar...")

    res = 0

    for par in pares:
        inicio = par[0]
        destino = par[1]
        longitud = shortest_path(u, inicio, destino)
        res += longitud

        print(f"Inicio: {inicio}, Destino: {destino}, Longitud: {longitud}")

    print(f"\nEl resultado es: {res}")
