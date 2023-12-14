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

print(lines)

seeds = []
sed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

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
