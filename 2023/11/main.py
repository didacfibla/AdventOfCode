from collections import deque
from itertools import combinations


def load_data():
    universe = [list(line.rstrip('\n')) for line in open("input", "r")]
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
    u, g = load_data()

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
