def hash(string: str) -> int:
    current = 0
    for ch in string:
        # Get the ASCI code for character
        ascii_value = ord(ch)
        # increase current adding the ASCI code obtained
        current += ascii_value
        # current value multiplies itself by 17
        current *= 17
        # set the current value to the remainer (%) of dividing itsels by 256
        current = current % 256
    return current


def part1(filename):
    data = open(filename, "r").readline().rstrip().split(",")

    total = 0
    for string in data:
        total += hash(string)

    print(f"Part 1: {total}")


def part2(filename: str):
    data = open(filename, "r").readline().rstrip().split(",")
    boxes = [{} for _ in range(256)]

    for ins in data:
        label = ''.join(char for char in ins if char.isalpha())
        focal_length = ''.join(char for char in ins if char.isdigit())
        operation = ''.join(char for char in ins if not char.isalnum() and not char.isspace())
        destination_box = hash(label)

        # print(f"label: {label}, Operation: {operation}, Focal_length: {focal_length}, Destination_box: {destination_box}")

        if operation == '-':
            boxes[destination_box].pop(label, None)

        elif operation == '=':
            boxes[destination_box][label] = focal_length

        else:
            print("Everything is wrong")

    # Calculate the final result:
    total = 0
    for box_num, box in enumerate(boxes):
        if len(box) > 0:
            elem_index = 1
            for value in box.keys():
                result = (box_num + 1) * elem_index * int(box.get(value))
                # print(f"{value}: {box_num + 1} (box {box_num}) * {elem_index} (x slot) * {box.get(value)} (focal length) = {(box_num + 1) * elem_index * int(box.get(value))} --> {result}")
                elem_index += 1
                total += result

    print(f"Part 2: {total}")


if __name__ == "__main__":
    part1("example")
    part2("input")
