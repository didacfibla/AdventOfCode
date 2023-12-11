import re

f = open("input.txt", "r")
lines = [linea.rstrip('\n') for linea in f]

races = []

durations = re.findall(r'\d+', lines[0])
records = re.findall(r'\d+', lines[1])

for duration in durations:
    races.append([int(duration)])

for i in range(0, len(records)):
    races[i].append(int(records[i]))

total = 1
for duration, record in races:
    win = 0

    for i in range(1, duration):
        #print(f"\tHold {i} sec. -> {duration - i} secs left. -> Max travel {i * (duration - i)} -> WIN: {i * (duration - i) > record}")
        if i * (duration - i) > record:
            win += 1
    total *= win
    print(f"Tiempo disponible: {duration}s Record actual: {record}. Formas de superar el record: {total}")

print(total)