import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def update_tail_position(head, tail):
    head_x = head[0]
    head_y = head[1]
    tail_x = tail[0]
    tail_y = tail[1]

    if head_x == tail_x:
        if head_y - tail_y >= 2:
            tail_y += 1
        elif tail_y - head_y >= 2:
            tail_y -= 1
    elif head_y == tail_y:
        if head_x - tail_x >= 2:
            tail_x += 1
        elif tail_x - head_x >= 2:
            tail_x -= 1
    else:
        if head_y - tail_y >= 2:
            tail_y += 1
            tail_x += 1 if head_x > tail_x else -1
        elif tail_y - head_y >= 2:
            tail_y -= 1
            tail_x += 1 if head_x > tail_x else -1
        elif head_x - tail_x >= 2:
            tail_x += 1
            tail_y += 1 if head_y > tail_y else -1
        elif tail_x - head_x >= 2:
            tail_x -= 1
            tail_y += 1 if head_y > tail_y else -1

    tail[0] = tail_x
    tail[1] = tail_y

if __name__ == "__main__":
    input = load_input()

    head = [0, 0]
    knots = [[0,0] for i in range(9)]

    visited_locations_part_1 = set()
    visited_locations_part_2 = set()

    for instruction in input:
        parts = instruction.split(" ")
        direction = parts[0]
        distance = int(parts[1])

        for i in range(distance):
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "R":
                head[0] += 1
            else:
                print("Unknown instruction: " + instruction)

            previous_knot = head
            for knot in knots:
                update_tail_position(previous_knot, knot)
                previous_knot = knot

            visited_locations_part_1.add(str(knots[0][0]) + "," + str(knots[0][1]))
            visited_locations_part_2.add(str(knots[-1][0]) + "," + str(knots[-1][1]))


    print(len(visited_locations_part_1))
    print(len(visited_locations_part_2))
