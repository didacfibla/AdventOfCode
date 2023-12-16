import re

pattern = re.compile("\\d+")


def parse_inputs(data: list[str]) -> list[list[str]]:
    as_text = "\n".join(data)
    return [line.split("\n") for line in as_text.split("\n\n")]


def find_locations(data: list[str]) -> int:
    """
    Parse input back to str, and split by \n\n to get the
    mappings easier
    """
    sections = parse_inputs(data)
    seeds = {x: x for x in map(int, pattern.findall(sections[0][0]))}
    for mapping in sections[1:]:
        for seed, value in seeds.items():
            for _range in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_range)))
                if src <= value < (src + length):
                    seeds[seed] = dest + (value - src)
    return min(seeds.values())


def part_one(input_data: list[str]):
    answer = find_locations(input_data)
    print(answer)


if __name__ == "__main__":
    data = [line.rstrip() for line in open("example").readlines()]
    part_one(data)
