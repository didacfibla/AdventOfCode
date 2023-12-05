import re


def part1():
    """
    Realiza la parte 1 del procesamiento del archivo de entrada.
    Suma los primeros y últimos dígitos de los números encontrados en cada línea.
    """
    with open("input.txt", "r") as f:
        lines = f.readlines()

    total_sum = 0

    for line in lines:
        line = line.rstrip()

        # Filtra los dígitos de la línea y toma el primer y último dígito
        digits = ''.join(filter(str.isdigit, line))
        number = int(f"{digits[0]}{digits[-1]}")

        total_sum += number
        print(f">>> Line: {line} -> {number} - Total Sum: {total_sum}")
    return total_sum


def part2():
    """
    Realiza la parte 2 del procesamiento del archivo de entrada.
    Convierte palabras numéricas a números y suma el primer y último valor encontrado en cada línea.
    """
    with open("input.txt", "r") as f:
        lines = f.readlines()

    valores = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    total_sum = 0

    for line in lines:
        line = line.rstrip()

        # Busca todas las posibles coincidencias permitiendo superposiciones, el \d indica digitos numericos
        valores_encontrados = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line, re.IGNORECASE)

        # Obtiene solo los grupos de captura de la coincidencia
        first_value = valores.get(valores_encontrados[0])
        second_value = valores.get(valores_encontrados[-1])

        value_to_add = int(str(first_value) + str(second_value))  # concatenamos los dos numeros  1 y 2 = 12. No 3, cuidado.
        total_sum += value_to_add

        print(f"Line: {line} --> Matches: {valores_encontrados} --> ({first_value}, {second_value}) - {value_to_add} - Total Sum: {total_sum}")
    return total_sum


if __name__ == '__main__':
    value1 = part1()
    value2 = part2()
    print()
    print(f"Resultado parte1: {value1}")
    print(f"Resultado parte2: {value2}")
