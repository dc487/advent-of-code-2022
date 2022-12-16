import pathlib
import math

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n")

class Monkey:
    def __init__(self, input):
        lines = input.splitlines()
        self.id = int(lines[0].split("Monkey ")[1][0])
        self.items = [int(x) for x in lines[1].split("Starting items: ")[1].split(", ")]
        operation = lines[2].split("Operation: new = ")[1]
        operation_split = operation.split(" ")
        self.operation_lhs = operation_split[0]
        self.operation_operator = operation_split[1]
        self.operation_rhs = operation_split[2]
        self.test_modulus = int(lines[3].split("Test: divisible by ")[1])
        self.true_monkey = int(lines[4].split("If true: throw to monkey ")[1])
        self.false_monkey = int(lines[5].split("If false: throw to monkey ")[1])
        self.worry_modulus = 1
        self.inspection_count = 0

    def has_items(self):
        return len(self.items) > 0

    def inspect_next_item(self):
        self.inspection_count += 1

        item = self.items.pop(0)
        worry_level = 0

        if self.operation_lhs == "old":
            worry_level = item
        else:
            worry_level = int(self.operation_lhs)

        if self.operation_operator == "*":
            if self.operation_rhs == "old":
                worry_level *= item
            else:
                worry_level *= int(self.operation_rhs)
        elif self.operation_operator == "+":
            if self.operation_rhs == "old":
                worry_level += item
            else:
                worry_level += int(self.operation_rhs)
        else:
            print("Unknown operator: " + self.operation_operator)

        # part 1
        #worry_level = math.floor(worry_level / 3)

        # part 2
        worry_level %= self.worry_modulus
        return worry_level

    def throw_item(self, item):
        if item % self.test_modulus == 0:
            return self.true_monkey
        else:
            return self.false_monkey

    def catch_item(self, item):
        self.items.append(item)


if __name__ == "__main__":
    input = load_input().split("\n\n")

    monkeys = [Monkey(m) for m in input]

    worry_modulus = 1
    for m in monkeys:
        worry_modulus *= m.test_modulus

    for m in monkeys:
        m.worry_modulus = worry_modulus

    for round in range(10000):
        for monkey in monkeys:
            while(monkey.has_items()):
                next_item = monkey.inspect_next_item()
                next_monkey = monkey.throw_item(next_item)
                monkeys[next_monkey].catch_item(next_item)

    inspection_counts = [m.inspection_count for m in monkeys]
    print(inspection_counts)
    inspection_counts.sort(reverse=True)
    print(inspection_counts[0] * inspection_counts[1])





