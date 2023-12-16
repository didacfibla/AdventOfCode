with open("example", "r") as f:
    mosaic = [list(line.rstrip('\n')) for line in f]

for line in mosaic:
    print(line)

start = next(((i, j) for i, row in enumerate(mosaic) for j, elem in enumerate(row) if elem == 'S'), None)
print(f"'S' encontrado en las posiciones: {start}")


