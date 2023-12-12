from functools import cmp_to_key

f = open("input.txt", "r")
lines = [linea.rstrip('\n') for linea in f]


def get_type(cadena: str) -> int:
    # Five of a Kind
    if any(cadena.count(char) == 5 for char in set(cadena)):
        return 5

    # Four of a Kind
    elif any(cadena.count(char) == 4 for char in set(cadena)):
        return 4

    # Full House
    elif len(set(cadena)) == 2 and any(cadena.count(char) == 3 for char in set(cadena)):
        return 3

    # Three of a Kind
    elif any(cadena.count(char) == 3 for char in set(cadena)):
        return 3

    # Two Pair
    elif len(set(cadena)) == 3 and any(cadena.count(char) == 2 for char in set(cadena)):
        return 2

    # One Pair
    elif len(set(cadena)) == 4:
        return 1

    # High Card
    else:
        return 0


def clave_ordenacion(cadena):
    prioridades = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    prioridades_lista = [prioridades.get(caracter, 0) for caracter in cadena]
    return prioridades_lista, cadena


if __name__ == '__main__':

    puntuations = {0: [],
                   1: [],
                   2: [],
                   3: [],
                   4: [],
                   5: []}

    datos = {}

    # Cogemos todas las manos y las clasificacmos
    for line in lines:
        hand, bid = line.split()
        datos[hand] = int(bid)
        puntuations.get(get_type(hand)).append(hand)

    # Cogemos cada clasificacion y las ordenamos por prioridad
    rank = 1
    total = 0
    for key in puntuations.keys():
        manos_clasificadas = puntuations.get(key)
        if len(manos_clasificadas) > 0:
            manos_ordenadas = sorted(manos_clasificadas, key=clave_ordenacion, reverse=False)
            print(f"Tipo {key}: {manos_clasificadas} -> {manos_ordenadas}")
            for mano in manos_ordenadas:
                print(f"{mano} rank{rank} -> {rank} * {datos[mano]} = {rank * datos[mano]}")
                total += rank * datos[mano]
                rank += 1
    print(total)