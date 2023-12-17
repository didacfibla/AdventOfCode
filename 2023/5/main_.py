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
    seeds_ = sections[0][0].split()[1:]
    seeds = {}

    for i in range(1, len(seeds_)):
        seeds.update({j: j for j in range(int(seeds_[i - 1]), int(seeds_[i]) + 1)})

    for mapping in sections[1:]:
        for seed, seed_value in seeds.items():
            for _ in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_)))
                if src <= seed_value < (src + length):
                    seeds[seed] = dest + (seed_value - src)

    print(min(seeds.values()))


if __name__ == "__main__":
    data = [line.rstrip() for line in open("input").readlines()]
    # part_one(data)
    part_two(data)
