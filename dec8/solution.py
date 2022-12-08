fhand = open("input.txt")

grid = []

for line in fhand:
    current_row = []
    trees = line.strip()
    for tree in trees:
        current_row.append(int(tree))
    grid.append(current_row)


no_of_visible_trees = 0


def visible_from_left(val_idx, array):
    val = array[val_idx]
    left_vals = array[:val_idx]
    for left_val in left_vals:
        if left_val >= val:
            return False

    return True


assert visible_from_left(0, [3, 0, 3, 7, 3]) == True
assert visible_from_left(1, [3, 0, 3, 7, 3]) == False
assert visible_from_left(2, [3, 0, 3, 7, 3]) == False
assert visible_from_left(3, [3, 0, 3, 7, 3]) == True
assert visible_from_left(4, [3, 0, 3, 7, 3]) == False


def visible_from_right(val_idx, array):
    val = array[val_idx]
    right_vals = array[val_idx + 1 :]
    for right_val in right_vals:
        if right_val >= val:
            return False

    return True


assert visible_from_right(0, [3, 0, 3, 7, 3]) == False
assert visible_from_right(1, [3, 0, 3, 7, 3]) == False
assert visible_from_right(2, [3, 0, 3, 7, 3]) == False
assert visible_from_right(3, [3, 0, 3, 7, 3]) == True
assert visible_from_right(4, [3, 0, 3, 7, 3]) == True


def visible_from_up(row_idx, col_idx, grid):
    val = grid[row_idx][col_idx]

    up_vals = []

    for i in range(row_idx):
        up_vals.append(grid[i][col_idx])

    for up_val in up_vals:
        if up_val >= val:
            return False

    return True


example_grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]
assert visible_from_up(1, 2, example_grid) == True
assert visible_from_up(1, 3, example_grid) == False


def visible_from_down(row_idx, col_idx, grid):
    val = grid[row_idx][col_idx]

    no_of_rows = len(grid)

    down_vals = []

    for i in range(row_idx + 1, no_of_rows):
        down_vals.append(grid[i][col_idx])

    for down_val in down_vals:
        if down_val >= val:
            return False

    return True


assert visible_from_down(3, 3, example_grid) == False
assert visible_from_down(4, 3, example_grid) == True

no_of_rows = len(grid)
no_of_cols = len(grid[0])
no_of_visible_trees = 0

for r in range(no_of_rows):
    for j in range(no_of_cols):
        if (
            visible_from_left(j, grid[r])
            or visible_from_right(j, grid[r])
            or visible_from_up(r, j, grid)
            or visible_from_down(r, j, grid)
        ):
            no_of_visible_trees += 1


print("Answer to puzzle 1: ", no_of_visible_trees)


################## PUZZLE 2 #######################


def no_visible_from_left(val_idx, array):
    val = array[val_idx]
    left_vals = array[:val_idx]

    visible_vals = 0

    for left_val in reversed(left_vals):
        if left_val >= val:
            return visible_vals + 1
        else:
            visible_vals += 1

    return visible_vals


assert no_visible_from_left(2, [2, 5, 5, 1, 2]) == 1
assert no_visible_from_left(4, [2, 5, 5, 1, 2]) == 2


def no_visible_from_right(val_idx, array):
    val = array[val_idx]
    right_vals = array[val_idx + 1 :]

    visible_vals = 0

    for right_val in right_vals:
        if right_val >= val:
            return visible_vals + 1
        else:
            visible_vals += 1

    return visible_vals


assert no_visible_from_right(2, [2, 5, 5, 1, 2]) == 2
assert no_visible_from_right(4, [2, 5, 5, 1, 2]) == 0
assert no_visible_from_right(1, [2, 5, 5, 1, 2]) == 1


def no_visible_from_up(row_idx, col_idx, grid):
    val = grid[row_idx][col_idx]

    up_vals = []

    visible_vals = 0

    for i in range(row_idx):
        up_vals.append(grid[i][col_idx])

    for up_val in reversed(up_vals):
        if up_val >= val:
            return visible_vals + 1
        else:
            visible_vals += 1

    return visible_vals


assert no_visible_from_up(1, 2, example_grid) == 1
assert no_visible_from_up(3, 2, example_grid) == 2


def no_visible_from_down(row_idx, col_idx, grid):
    val = grid[row_idx][col_idx]

    no_of_rows = len(grid)

    down_vals = []

    visible_vals = 0

    for i in range(row_idx + 1, no_of_rows):
        down_vals.append(grid[i][col_idx])

    for down_val in down_vals:
        if down_val >= val:
            return visible_vals + 1
        else:
            visible_vals += 1

    return visible_vals


assert no_visible_from_down(1, 2, example_grid) == 2
assert no_visible_from_down(3, 2, example_grid) == 1


scenic_score = []

for r in range(no_of_rows):
    for j in range(no_of_cols):
        score = (
            no_visible_from_left(j, grid[r])
            * no_visible_from_right(j, grid[r])
            * no_visible_from_up(r, j, grid)
            * no_visible_from_down(r, j, grid)
        )
        scenic_score.append(score)


print("Answer to puzzle 2: ", sorted(scenic_score, reverse=True)[0])
