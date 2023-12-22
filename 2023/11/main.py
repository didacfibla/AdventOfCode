import sys
from collections import deque
from itertools import combinations


def load_data(filename):
    # Load the universe
    universe = [list(line.rstrip('\n')) for line in open(filename, "r")]

    # Locate galaxies
    galaxies = [(r, c) for r, row in enumerate(universe) for c, ch in enumerate(row) if ch == '#']

    # Locate row formed only by '.'
    empty_rows = [r for r, row in enumerate(universe) if all(ch == "." for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*universe)) if all(ch == "." for ch in col)]

    total = 0
    scale = 1000000

    # Recorremos cada posible par de galaxias y calculamos la distancia
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:  # manhattan distance formula (|P2x - P1x| + |P2y + P2y|) give us distane between two points in a xy plane
            # Si la fila o columna esta vacia, la expandimos
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1

            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1

    print(total)


if __name__ == "__main__":
    load_data("input")
