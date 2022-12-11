import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    cycles = []

    for instruction in input:
        cycles.append(0)
        if instruction.startswith("addx"):
            cycles.append(int(instruction.split(" ")[1]))

    print(sum([(1 + sum(cycles[:i*40 + 19])) * ((i*40) + 20) for i in range(6)]))

    x = 1
    drawing = []
    for cycle_number, cycle_addition in enumerate(cycles):
        n = cycle_number % 40
        if x - 1 <= n and x + 1 >= n:
            drawing.append('#')
        else:
            drawing.append('.')
        x += cycle_addition
        
    for y in range(6):
        print(''.join(drawing[y * 40:(y+1) * 40]))
