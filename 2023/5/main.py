from itertools import zip_longest

seeds = []
sed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

sed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temperature_map = {}
temperature_to_humidity_map = {}
humidity_to_location_map = {}


def get_input_data_to_list():
    lines = open("input", 'r').read()
    lines = lines.replace('\n\n', '\n')
    lines = lines.replace('\n', ' ')
    lines = lines.replace(' map:', '')
    lines = lines.replace('seeds: ', '')
    lines = lines.split()

    # convertirmos los numeros a int
    for i in range(0, len(lines)):
        if lines[i].isdigit():
            lines[i] = int(lines[i])

    # print(lines)

    # Cargamos las semillas
    i = 0
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        seeds.append(lines[i])
        i += 1

    print(f"Seeds: {seeds}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        sed_to_soil.append(lines[i])
        i += 1
    print(f"sed_to_soil: {sed_to_soil}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        soil_to_fertilizer.append(lines[i])
        i += 1
    print(f"soil_to_fertilizer: {soil_to_fertilizer}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        fertilizer_to_water.append(lines[i])
        i += 1
    print(f"fertilizer_to_water: {fertilizer_to_water}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        water_to_light.append(lines[i])
        i += 1
    print(f"water_to_light: {water_to_light}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        light_to_temperature.append(lines[i])
        i += 1
    print(f"light_to_temperature: {light_to_temperature}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        temperature_to_humidity.append(lines[i])
        i += 1
    print(f"temperature_to_humidity: {temperature_to_humidity}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        humidity_to_location.append(lines[i])
        i += 1
        if i == len(lines): break
    print(f"humidity_to_location: {humidity_to_location}")


def prepare_input():
    sed_to_soil_3 = zip_longest(*[iter(sed_to_soil)] * 3, fillvalue=None)
    for elem in sed_to_soil_3:
        inicio1 = elem[0]
        inicio2 = elem[1]
        rango = elem[2]


if __name__ == "__main__":
    get_input_data_to_list()
    prepare_input()
