fhand = open("input.txt")

cycle = 0
x = 1
cycle_values = dict()


def calculate_signal_strength(cycle_no, cycle_val):
    return cycle_no * cycle_val


for line in fhand:
    command = line.strip()
    if "noop" in command:
        cycle += 1
        cycle_values[cycle] = x
    else:
        cycle_values[cycle + 1] = x
        cycle_values[cycle + 2] = x

        cycle += 2
        v1, v2 = line.split(" ")
        x += int(v2)


p1 = 0
for i in range(20, 260, 40):
    p1 += calculate_signal_strength(i, cycle_values[i])

print("Answer to puzzle 1 ", p1)

# PUZZLE 2


crt_screen = []
cycle_count = 1
for i in range(1, 7):
    crt_screen.append(["."] * 40)
    for j in range(40):
        cycle_value = cycle_values[cycle_count]
        value_to_draw = "."
        if abs(cycle_value - j) <= 1:
            value_to_draw = "#"
        crt_screen[i - 1][j] = value_to_draw
        cycle_count += 1


for line in crt_screen:
    print("".join(line))
