import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    count_part1 = 0
    count_part2 = 0
    for line in input:
        elves = line.split(",")
        elf1_numbers = elves[0].split("-")
        elf2_numbers = elves[1].split("-")
        low_elf_1 = int(elf1_numbers[0])
        high_elf_1 = int(elf1_numbers[1])
        low_elf_2 = int(elf2_numbers[0])
        high_elf_2 = int(elf2_numbers[1])

        if (low_elf_1 <= low_elf_2 and high_elf_1 >= high_elf_2) or (low_elf_2 <= low_elf_1 and high_elf_2 >= high_elf_1):
            count_part1 += 1

        if (low_elf_1 <= low_elf_2 and low_elf_2 <= high_elf_1) or (low_elf_2 <= low_elf_1 and low_elf_1 <= high_elf_2):
            count_part2 += 1

    print(count_part1)
    print(count_part2)
