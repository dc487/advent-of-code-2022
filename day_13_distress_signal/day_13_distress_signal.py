import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").split('\n\n')

def parse_packet(packet):
    if '[' not in packet:
        return int(packet)
        
    parsed_items = []
    
    # trim the opening and closing []
    packet = packet[1:-1]

    open_bracket_count = 0
    i = 0
    current_item = ''
    while i < len(packet):
        if open_bracket_count == 0 and packet[i] == ',':
            if current_item != '':
                parsed_items.append(parse_packet(current_item))
            current_item = ''
        else:
            current_item += packet[i]
            if packet[i] == '[':
                open_bracket_count += 1
            elif packet[i] == ']':
                open_bracket_count -= 1
        i += 1

    if current_item != '':
        parsed_items.append(parse_packet(current_item))

    return parsed_items

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return b - a
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    else:
        for i in range(len(a)):
            if i >= len(b):
                return -1

            comparison = compare(a[i], b[i])
            if comparison > 0:
                return 1
            elif comparison < 0:
                return -1

        return len(b) - len(a)


def bubble_sort(list):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(len(list) - 1):
            if compare(list[i], list[i + 1]) < 0:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                swap_occurred = True


if __name__ == "__main__":
    input = [x.split('\n') for x in load_input()]

    packets = []
    correct_pair_total = 0
    for pair_index, pair in enumerate(input):
        a = parse_packet(pair[0])
        b = parse_packet(pair[1])
        packets.append(a)
        packets.append(b)
        
        if compare(a, b) >= 0:
            correct_pair_total += pair_index + 1

    print(correct_pair_total)

    marker1 = [[2]]
    marker2 = [[6]]
    packets.append(marker1)
    packets.append(marker2)

    bubble_sort(packets)
    
    index1 = packets.index(marker1) + 1
    index2 = packets.index(marker2) + 1
    print(index1 * index2)

    