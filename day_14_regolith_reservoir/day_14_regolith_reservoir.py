import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def print_grid(grid):
    for y in range(len(grid)):
        line = str(y) + ' '
        for x in range(len(grid[0])):
            line += grid[y][x]
        print(line)

def simulate_sand_fall(grid, min_x, max_y):
    sand_fallen_through = False
    grain_number = 0
    while not sand_fallen_through:
        grain_number += 1
        sand_stopped = False
        current_x = 500 - min_x
        current_y = 0

        if grid[current_y][current_x] == 'O':
            # We've filled up the map!
            break

        while not sand_stopped:
            if current_y + 1 > max_y:
                sand_fallen_through = True
                break

            if grid[current_y + 1][current_x] == '.':
                current_y += 1
            elif grid[current_y + 1][current_x - 1] == '.':
                current_y += 1
                current_x -= 1
            elif grid[current_y + 1][current_x + 1] == '.':
                current_y += 1
                current_x += 1
            else:
                grid[current_y][current_x] = 'O'
                sand_stopped = True
 
    print_grid(grid)
    return grain_number - 1

if __name__ == "__main__":
    input = load_input()

    all_x = set()
    all_y = set()

    line_pairs = []

    for line in input:
        coords = [[x.split(',')[0], x.split(',')[1]] for x in line.split(' -> ')]
        for i in range(len(coords) - 1):
            x1 = int(coords[i][0])
            y1 = int(coords[i][1])
            x2 = int(coords[i + 1][0])
            y2 = int(coords[i + 1][1])
            all_x.add(x1)
            all_x.add(x2)
            all_y.add(y1)
            all_y.add(y2)

            line_pairs.append(((x1, y1), (x2, y2)))

    min_x = min(all_x)
    min_y = 0
    max_x = max(all_x)
    max_y = max(all_y)

    width = max_x - min_x
    height = max_y

    grid = [['.' for i in range(width + 1)] for j in range(height + 1)]

    for line_pair in line_pairs:
        x1 = line_pair[0][0] - min_x
        y1 = line_pair[0][1]
        x2 = line_pair[1][0] - min_x
        y2 = line_pair[1][1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = '#'
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = '#'

    
    total_grains = simulate_sand_fall(grid, min_x, max_y)
    print(total_grains)

    min_x = 0
    min_y = 0
    max_x = max(all_x)
    max_y = max(all_y)

    width = 1000
    height = max_y

    grid = [['.' for i in range(width + 1)] for j in range(height + 1)]

    for line_pair in line_pairs:
        x1 = line_pair[0][0] - min_x
        y1 = line_pair[0][1]
        x2 = line_pair[1][0] - min_x
        y2 = line_pair[1][1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = '#'
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = '#'

    max_y += 2
    grid.append(['.' for i in range(width + 1)])
    grid.append(['#' for i in range(width + 1)])

    total_grains = simulate_sand_fall([y[:] for y in grid], min_x, max_y)
    print(total_grains)
