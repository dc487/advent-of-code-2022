import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()[0]

    for index in range(len(input) - 3):
        if len(set(input[index:index + 4])) == 4:
            print(index + 4)
            break

    for index in range(len(input) - 13):
        if len(set(input[index:index + 14])) == 14:
            print(index + 14)
            break
        
