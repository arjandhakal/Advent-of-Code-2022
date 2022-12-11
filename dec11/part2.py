import re

fhand = open("input.txt")

"""
Data Structure

monkeys = {
    1: {
        items: []
        operation: {
            a: old,
            operator: +,
            b: old
        },
        test:{
            divisibleBy: x,
            true: 1
            false: 3
        }
    }
}
"""


def plus(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = {"*": multiply, "+": plus}

monkeys = {}

current_monkey = None

for line in fhand:
    line = line.strip()
    if "Monkey" in line:
        new_monkey = dict()
        monkey_no = int(re.findall("\d+", line)[0])
        current_monkey = monkey_no
        monkeys[current_monkey] = dict()
        monkeys[current_monkey]["test"] = {}

    if "Starting" in line:
        items = [int(x) for x in re.findall("\d+", line)]
        monkeys[current_monkey]["items"] = items

    if "Operation" in line:
        operation = re.search("(old\s.\s\d*|old)", line)
        operation = operation.group()
        operation = operation.split(" ")
        a = operation[0] if operation[0] == "old" else int(a)
        operator = operation[1]
        b = "old" if operation[2] == "" else int(operation[2])

        monkeys[current_monkey]["operation"] = {"a": a, "operator": operator, "b": b}

    if "divisible" in line:
        divisible_by = int(re.findall("\d+", line)[0])
        monkeys[current_monkey]["test"]["divisibleBy"] = divisible_by
    if "true" in line:
        monkey_no = int(re.findall("\d+", line)[0])
        monkeys[current_monkey]["test"]["true"] = monkey_no
    if "false" in line:
        monkey_no = int(re.findall("\d+", line)[0])
        monkeys[current_monkey]["test"]["false"] = monkey_no


monkeys_investigation_count = {}

for monkey, _ in monkeys.items():
    monkeys_investigation_count[monkey] = 0


def increase_investigation_count(monkey_no, no_of_items):
    monkeys_investigation_count[monkey_no] += no_of_items


def investigate_item(item, operation_attr):

    operator = operations[operation_attr["operator"]]
    a = item if operation_attr["a"] == "old" else operation_attr["a"]
    b = item if operation_attr["b"] == "old" else operation_attr["b"]

    return operator(a, b)


def test_item(item, divisible_by):
    return item % divisible_by == 0


def get_monkey_after_test(result, current_monkey):
    if result:
        return current_monkey["test"]["true"]
    else:
        return current_monkey["test"]["false"]


def start_round(divisible_multiple):
    for monkey_no, monkey_attributes in monkeys.items():
        monkey_items = monkey_attributes["items"]

        monkey_operation_attr = monkey_attributes["operation"]

        increase_investigation_count(monkey_no, len(monkey_items))

        divisible_by = monkey_attributes["test"]["divisibleBy"]

        for item in monkey_items:
            item = investigate_item(item, monkey_operation_attr)

            is_divisible = test_item(item, divisible_by)

            item = item % divisible_multiple

            monkey_to_pass_to = monkeys[
                get_monkey_after_test(is_divisible, monkey_attributes)
            ]

            monkey_to_pass_to["items"].append(item)

        monkey_items = []
        monkeys[monkey_no]["items"] = monkey_items


divisible_multiple = 1

for k, v in monkeys.items():
    divisible_multiple *= v["test"]["divisibleBy"]

for i in range(10_000):
    start_round(divisible_multiple)


p2 = []

for k, v in monkeys_investigation_count.items():
    p2.append(v)

p2 = sorted(p2, reverse=True)

print("Answer to puzzle 1: ", p2[0] * p2[1])
