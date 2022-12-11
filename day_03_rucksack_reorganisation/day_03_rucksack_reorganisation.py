import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = [[ord(y) - 96 if ord(y) > 96 else ord(y) - 64 + 26 for y in x] for x in load_input()]

    priority_sum = 0
    for bag in input:
        compartment_1 = bag[:len(bag)//2]
        compartment_2 = bag[len(bag)//2:]

        for item in compartment_1:
            if item in compartment_2:
                priority_sum += item
                break
        
    print(priority_sum)
    
    priority_sum = 0
    for i in range(len(input) // 3):
        index = 3 * i
        bag1 = input[index]
        bag2 = input[index + 1]
        bag3 = input[index + 2]

        for item in bag1:
            if item in bag2 and item in bag3:
                priority_sum += item
                break

    print(priority_sum)