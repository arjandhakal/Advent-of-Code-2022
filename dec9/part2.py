fhand = open("input.txt")

NO_OF_KNOTS = 10
moved_positions = []
current_positions = []

for i in range(NO_OF_KNOTS):
    current_positions.append((0, 0))


def calculate_new_head_pos(head_pos, direction):
    h_x, h_y = head_pos
    if direction == "U":
        h_y += 1
    elif direction == "L":
        h_x -= 1
    elif direction == "R":
        h_x += 1
    else:
        h_y -= 1
    return (h_x, h_y)


def calculate_new_tail_pos(head, tail):
    h_x, h_y = head
    t_x, t_y = tail
    diff_in_x = abs(h_x - t_x)
    diff_in_y = abs(h_y - t_y)

    if diff_in_x <= 1 and diff_in_y <= 1:
        return t_x, t_y

    x_dir = 1
    y_dir = 1

    if h_y < t_y:
        y_dir = -1
    if h_x < t_x:
        x_dir = -1

    if h_x == t_x:
        t_y += y_dir
        return t_x, t_y
    if h_y == t_y:
        t_x += x_dir
        return t_x, t_y

    t_x += x_dir
    t_y += y_dir

    return calculate_new_tail_pos(head, (t_x, t_y))


last_tail_pos = set()


for line in fhand:
    direction, steps = line.strip().split(" ")
    steps = int(steps)

    for step in range(steps):
        current_h = calculate_new_head_pos(current_positions[0], direction)
        current_positions[0] = current_h
        for i in range(0, NO_OF_KNOTS - 1):
            head = current_positions[i]
            tail = current_positions[i + 1]
            current_t = calculate_new_tail_pos(head, tail)
            current_positions[i + 1] = current_t

            last_tail_pos.add(current_positions[NO_OF_KNOTS - 1])

print(len(last_tail_pos))
