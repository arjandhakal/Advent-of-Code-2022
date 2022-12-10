fhand = open("input.txt")


moved_positions = []

current_h = (0, 0)  # current head position
current_t = (0, 0)  # current tail position

moved_positions.append([current_h, current_t])


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


for line in fhand:
    direction, steps = line.strip().split(" ")
    steps = int(steps)

    # for puzzle 1
    for step in range(steps):
        current_h = calculate_new_head_pos(current_h, direction)
        current_t = calculate_new_tail_pos(current_h, current_t)
        moved_positions.append([current_h, current_t])


def find_all_tail_visited(m_pos):
    t_pos = set()
    for pos in m_pos:
        T = pos[len(pos) - 1]
        t_pos.add(T)
    return len(t_pos)


print("Answer to puzzle 1 : ", find_all_tail_visited(moved_positions))
