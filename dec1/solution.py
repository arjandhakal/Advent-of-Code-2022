from functools import reduce

fhand = open("input.txt")

current_calories = 0

elf_calories = []

for line in fhand:
    if line.strip() == "":
        elf_calories.append(current_calories)
        current_calories = 0
        continue

    current_calories += int(line.strip())


elf_calories = sorted(elf_calories, reverse=True)

# Solution to puzzle 1
print(elf_calories[0])

# Soluton to puzzle 2
print(reduce(lambda a, b: a + b, elf_calories[0:3]))
