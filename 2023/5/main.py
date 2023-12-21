import re
import sys

pattern = re.compile("\\d+")


def parse_inputs(data: list[str]) -> list[list[str]]:
    as_text = "\n".join(data)
    return [line.split("\n") for line in as_text.split("\n\n")]


def part_one(data):
    sections = parse_inputs(data)
    seeds = {x: x for x in map(int, pattern.findall(sections[0][0]))}

    for mapping in sections[1:]:
        for seed, seed_value in seeds.items():
            for _ in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_)))
                if src <= seed_value < (src + length):
                    seeds[seed] = dest + (seed_value - src)

    print(seeds)


def part_two(data):
    sections = parse_inputs(data)
    seeds_ranges = sections[0][0].split()[1:]
    seeds = []

    for i in range(0, len(seeds_ranges), 2):
        start = int(seeds_ranges[i])
        end = int(seeds_ranges[i]) + int(seeds_ranges[i + 1]) - 1
        seeds.append([start, end])

    for mapping in sections[1:]:

        print(mapping)

        for index, seed_range in enumerate(seeds):
            start, end = seed_range

            for _range in mapping[1:]:
                destination, source, length = list(map(int, pattern.findall(_range)))

                if source <= start and start < (source + length):
                    seeds[index][0] = destination + (start - source)

                    if end < source + length:
                        seeds[index][1] = destination + (end - source)

                    else:
                        seeds[index][1] = destination + length - 1
                        seeds.append([source + length, end])

                elif source <= end and end < (source + length):
                    seeds[index][1] = destination + (end - source)

                    if start > source:
                        seeds[index][0] = destination + (start - source)
                    else:
                        seeds[index][0] = destination
                        seeds.append([start, source - 1])

    print(min(min(seeds)))


if __name__ == "__main__":
    data = [line.rstrip() for line in open("input").readlines()]
    # part_one(data)
    part_two(data)
