import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    width = len(input[0])
    height = len(input)

    visible_count = 0
    max_scenic_score = 0
    for x in range(width):
        for y in range(height):
            current_tree = input[y][x]
            
            if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                visible_count += 1
                continue

            trees_above = [i[x] for i in input[y - 1::-1]]
            trees_below = [i[x] for i in input[y + 1:]]
            trees_left = input[y][x - 1::-1]
            trees_right = input[y][x + 1:]

            if max(trees_above) < current_tree or max(trees_below) < current_tree or max(trees_left) < current_tree or max(trees_right) < current_tree:
                visible_count += 1

            viewing_above = len(trees_above)
            for i, tree in enumerate(trees_above):
                if tree >= current_tree:
                    viewing_above = i + 1
                    break

            viewing_below = len(trees_below)
            for i, tree in enumerate(trees_below):
                if tree >= current_tree:
                    viewing_below = i + 1
                    break

            viewing_left = len(trees_left)
            for i, tree in enumerate(trees_left):
                if tree >= current_tree:
                    viewing_left = i + 1
                    break
                    
            viewing_right = len(trees_right)
            for i, tree in enumerate(trees_right):
                if tree >= current_tree:
                    viewing_right = i + 1
                    break

            current_scenic_score = viewing_above * viewing_below * viewing_left * viewing_right
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score

    print(visible_count)
    print(max_scenic_score)


