import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    elf_calories = []
    calory_count = 0
    for calory_entry in input:
        if calory_entry != "":
            calory_count += int(calory_entry)
        else:
            elf_calories.append(calory_count)
            calory_count = 0
    
    print(max(elf_calories))

    elf_calories.sort(reverse=True)
    print(elf_calories[0] + elf_calories[1] + elf_calories[2])
