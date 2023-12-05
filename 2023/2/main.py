MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def part1():
    VALID_GAMES = []

    for line in open("input.txt", "r").readlines():
        line = line.rstrip()
        game_id, cubes = line.split(":")

        print(game_id)

        ROJOS_TIRADOS = 0
        AZULES_TIRADOS = 0
        VERDES_TIRADOS = 0

        rondas = cubes.split(";")
        numero_ronda = 1

        for ronda in rondas:
            print(f"\tRonda {numero_ronda}", end=": ")
            tirada = ronda.split(" ")
            tirada_limpia = [elemento for elemento in tirada if len(elemento) >= 1]

            for i in range(0, len(tirada_limpia), 2):
                numero_cubos_sacados = int(tirada_limpia[i])
                color_cubos_sacados = tirada_limpia[i + 1]

                # aqui es donde tenemos el numero y el color
                if "blue" in color_cubos_sacados:
                    if AZULES_TIRADOS < numero_cubos_sacados:
                        AZULES_TIRADOS = numero_cubos_sacados

                elif "red" in color_cubos_sacados:
                    if ROJOS_TIRADOS < numero_cubos_sacados:
                        ROJOS_TIRADOS = numero_cubos_sacados

                elif "green" in color_cubos_sacados:
                    if VERDES_TIRADOS < numero_cubos_sacados:
                        VERDES_TIRADOS = numero_cubos_sacados

            numero_ronda += 1

            print(f"Rojo {ROJOS_TIRADOS}, Verde {VERDES_TIRADOS}, Azul {AZULES_TIRADOS}")

        if VERDES_TIRADOS > MAX_GREEN_CUBES or ROJOS_TIRADOS > MAX_RED_CUBES or AZULES_TIRADOS > MAX_BLUE_CUBES:
            print(f"\tJuego no valido ya que superamos el máximo de cubos de algun color")

        else:
            game_id_numer_only = game_id.split(' ')[1]
            VALID_GAMES.append(game_id_numer_only)
            print(f"\tEl juego {game_id_numer_only} es valido")

        print("--------------")

    # Mostramos los resultados
    print(VALID_GAMES)
    sum = 0
    for valid_game in VALID_GAMES:
        sum += int(valid_game)
    print(sum)
    return sum


def part2():
    total = 0

    for line in open("input.txt", "r").readlines():
        line = line.rstrip()
        game_id, cubes = line.split(":")

        print(game_id)

        ROJOS_TIRADOS = 0
        AZULES_TIRADOS = 0
        VERDES_TIRADOS = 0

        rondas = cubes.split(";")
        numero_ronda = 1

        for ronda in rondas:
            print(f"\tRonda {numero_ronda}", end=": ")
            tirada = ronda.split(" ")
            tirada_limpia = [elemento for elemento in tirada if len(elemento) >= 1]

            for i in range(0, len(tirada_limpia), 2):
                numero_cubos_sacados = int(tirada_limpia[i])
                color_cubos_sacados = tirada_limpia[i + 1]

                # aqui es donde tenemos el numero y el color
                if "blue" in color_cubos_sacados:
                    if AZULES_TIRADOS < numero_cubos_sacados:
                        AZULES_TIRADOS = numero_cubos_sacados

                elif "red" in color_cubos_sacados:
                    if ROJOS_TIRADOS < numero_cubos_sacados:
                        ROJOS_TIRADOS = numero_cubos_sacados

                elif "green" in color_cubos_sacados:
                    if VERDES_TIRADOS < numero_cubos_sacados:
                        VERDES_TIRADOS = numero_cubos_sacados

            numero_ronda += 1

            print(f"Rojo {ROJOS_TIRADOS}, Verde {VERDES_TIRADOS}, Azul {AZULES_TIRADOS}")

        print(f"\tCubos necesarios -> Verde: {VERDES_TIRADOS}, Rojo: {ROJOS_TIRADOS}, Azul: {AZULES_TIRADOS}")
        total += (VERDES_TIRADOS * ROJOS_TIRADOS * AZULES_TIRADOS)
        print(total)
        print("--------------")

    return total


if __name__ == '__main__':
    r1 = part1()
    r2 = part2()
    print(f"\npart1: {r1}")
    print(f"part2: {r2}")
