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

    # print(f"Seeds: {seeds}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        sed_to_soil.append(lines[i])
        i += 1
    # print(f"sed_to_soil: {sed_to_soil}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        soil_to_fertilizer.append(lines[i])
        i += 1
    # print(f"soil_to_fertilizer: {soil_to_fertilizer}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        fertilizer_to_water.append(lines[i])
        i += 1
    # print(f"fertilizer_to_water: {fertilizer_to_water}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        water_to_light.append(lines[i])
        i += 1
    # print(f"water_to_light: {water_to_light}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        light_to_temperature.append(lines[i])
        i += 1
    # print(f"light_to_temperature: {light_to_temperature}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        temperature_to_humidity.append(lines[i])
        i += 1
    # print(f"temperature_to_humidity: {temperature_to_humidity}")

    i += 1
    while isinstance(lines[i], (int, float)):
        # Si el elemento es un número, haz algo con él
        humidity_to_location.append(lines[i])
        i += 1
        if i == len(lines): break
    # print(f"humidity_to_location: {humidity_to_location}")


def generate_ranges(list_data):
    res = {}
    list_of_3 = zip_longest(*[iter(list_data)] * 3, fillvalue=None)
    for elem in list_of_3:
        f = elem[0]
        s = elem[1]
        r = elem[2]

        for i in range(0, r):
            res[s] = f
            s += 1
            f += 1

    return res


def prepare_input():
    global sed_to_soil_map
    global soil_to_fertilizer_map
    global fertilizer_to_water_map
    global water_to_light_map
    global light_to_temperature_map
    global temperature_to_humidity_map
    global humidity_to_location_map

    sed_to_soil_map = generate_ranges(sed_to_soil)
    soil_to_fertilizer_map = generate_ranges(soil_to_fertilizer)
    fertilizer_to_water_map = generate_ranges(fertilizer_to_water)
    water_to_light_map = generate_ranges(water_to_light)
    light_to_temperature_map = generate_ranges(light_to_temperature)
    temperature_to_humidity_map = generate_ranges(temperature_to_humidity)
    humidity_to_location_map = generate_ranges(humidity_to_location)


def get_correspodentcy(data_map: dict, key: int):
    return data_map.get(key, key)


if __name__ == "__main__":
    print("LOADING INPUT DATA....")
    get_input_data_to_list()

    print("GENERATIGN RANGES ....")
    prepare_input()

    print("CALCULATING LOCATIONS ...")
    locations = []

    for seed in seeds:
        soil = get_correspodentcy(sed_to_soil_map, seed)
        fertilizer = get_correspodentcy(soil_to_fertilizer_map, soil)
        water = get_correspodentcy(fertilizer_to_water_map, fertilizer)
        light = get_correspodentcy(water_to_light_map, water)
        temperature = get_correspodentcy(light_to_temperature_map, light)
        humidity = get_correspodentcy(temperature_to_humidity_map, temperature)
        location = get_correspodentcy(humidity_to_location_map, humidity)

        locations.append(location)
        print(f"Seed {seed} -> soil: {soil} -> fertilizer: {fertilizer} -> water: {water} -> light: {light} -> temperature: {temperature} -> humidity: {humidity} -> location: {location}")

    print(min(locations))
