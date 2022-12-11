import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = [x.replace(" ", "") for x in load_input()]

    scores_1 = {
        "AX": 1 + 3,
        "AY": 2 + 6,
        "AZ": 3 + 0,
        "BX": 1 + 0,
        "BY": 2 + 3,
        "BZ": 3 + 6,
        "CX": 1 + 6,
        "CY": 2 + 0,
        "CZ": 3 + 3
    }

    print(sum([scores_1[x] for x in input]))

    scores_2 = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7
    }

    print(sum([scores_2[x] for x in input]))
    