import pathlib
from queue import PriorityQueue

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    width = len(input[0])
    height = len(input)

    start_position = (0, 0)
    end_position = (0, 0)
    for y in range(height):
        for x in range(width):
            if input[y][x] == 'S':
                start_position = (x, y)
            elif input[y][x] == 'E':
                end_position = (x, y)

    visited = set()
    path_queue = PriorityQueue()
    path_queue.put((0, start_position))

    total_steps = 0
    while not path_queue.empty():
        (total_steps, current_position) = path_queue.get()
        x = current_position[0]
        y = current_position[1]

        if current_position == end_position:
            break

        if current_position in visited:
            continue

        visited.add(current_position)

        max_height = ord(input[y][x]) + 1
        if current_position == start_position:
            max_height = ord('a') + 1

        up = (x, y - 1)
        down = (x, y + 1)
        left = (x - 1, y)
        right = (x + 1, y)

        if up not in visited and up[1] >= 0:
            up_height = ord('z') if up == end_position else ord(input[up[1]][up[0]])
            if up_height <= max_height:
                path_queue.put((total_steps + 1, up))

        if down not in visited and down[1] < height:
            down_height = ord('z') if down == end_position else ord(input[down[1]][down[0]])
            if down_height <= max_height:
                path_queue.put((total_steps + 1, down))
            
        if left not in visited and left[0] >= 0:
            left_height = ord('z') if left == end_position else ord(input[left[1]][left[0]])
            if left_height <= max_height:
                path_queue.put((total_steps + 1, left))
            
        if right not in visited and right[0] < width:
            right_height = ord('z') if right == end_position else ord(input[right[1]][right[0]])
            if right_height <= max_height:
                path_queue.put((total_steps + 1, right))

    print(total_steps)


    # part two - go from end to any 'a'
    visited = set()
    path_queue = PriorityQueue()
    path_queue.put((0, end_position))

    total_steps = 0
    while not path_queue.empty():
        (total_steps, current_position) = path_queue.get()
        x = current_position[0]
        y = current_position[1]

        if input[y][x] == 'a':
            break

        if current_position in visited:
            continue

        visited.add(current_position)

        current_height = ord(input[y][x])
        if current_position == end_position:
            current_height = ord('z')

        up = (x, y - 1)
        down = (x, y + 1)
        left = (x - 1, y)
        right = (x + 1, y)

        if up not in visited and up[1] >= 0:
            up_height = ord('z') if up == end_position else ord(input[up[1]][up[0]])
            if up_height + 1 >= current_height:
                path_queue.put((total_steps + 1, up))

        if down not in visited and down[1] < height:
            down_height = ord('z') if down == end_position else ord(input[down[1]][down[0]])
            if down_height + 1 >= current_height:
                path_queue.put((total_steps + 1, down))
            
        if left not in visited and left[0] >= 0:
            left_height = ord('z') if left == end_position else ord(input[left[1]][left[0]])
            if left_height + 1 >= current_height:
                path_queue.put((total_steps + 1, left))
            
        if right not in visited and right[0] < width:
            right_height = ord('z') if right == end_position else ord(input[right[1]][right[0]])
            if right_height + 1 >= current_height:
                path_queue.put((total_steps + 1, right))

    print(total_steps)
