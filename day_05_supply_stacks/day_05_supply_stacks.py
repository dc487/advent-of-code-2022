import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    floor_line = 0
    for i in input:
        if (i.startswith(" 1 ")):
            break
        floor_line += 1

    number_of_stacks = int(input[floor_line][-2])

    stacks = [[] for x in range(number_of_stacks)]

    for index, stack in enumerate(stacks):
        for line in input[:floor_line]:
            item = line[4*index + 1]
            if item != " ":
                stack.insert(0, item)

    instructions = input[floor_line + 2:]

    for instruction in instructions:
        parts = instruction.split(" from ")
        count = int(parts[0].split(" ")[-1])
        stack_number_parts = parts[1].split(" to ")
        from_stack = int(stack_number_parts[0]) - 1
        to_stack = int(stack_number_parts[1]) - 1

        for i in range(count):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)


    print(''.join([x[-1] for x in stacks]))


    stacks = [[] for x in range(number_of_stacks)]

    for index, stack in enumerate(stacks):
        for line in input[:floor_line]:
            item = line[4*index + 1]
            if item != " ":
                stack.insert(0, item)

    for instruction in instructions:
        parts = instruction.split(" from ")
        count = int(parts[0].split(" ")[-1])
        stack_number_parts = parts[1].split(" to ")
        from_stack = int(stack_number_parts[0]) - 1
        to_stack = int(stack_number_parts[1]) - 1

        crates_to_move = []
        for i in range(count):
            crates_to_move.insert(0, stacks[from_stack].pop())
        
        stacks[to_stack].extend(crates_to_move)


    print(''.join([x[-1] for x in stacks]))