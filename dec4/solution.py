fhand = open("input.txt")


def check_fully_contains(intervals):
    """
    For intervals [(a,b),(c,d)] checks if c and d is contained by a and b
    """
    intervals = sorted(intervals)
    a, b = intervals[0]
    c, d = intervals[1]

    if (c >= a and d <= b) or (a >= c and b <= d):
        return True
    else:
        return False


def check_overlaps(intervals):
    """
    For intervals [(a,b),(c,d)] checks if they overlap
    """
    intervals = sorted(intervals)
    a, b = intervals[0]
    c, d = intervals[1]

    if c <= b or b >= c:
        return True
    else:
        return False


p1 = 0
p2 = 0

for line in fhand:
    l = [x.split("-") for x in line.strip().split(",")]
    pair_sections = [[int(l[0][0]), int(l[0][1])], [int(l[1][0]), int(l[1][1])]]

    if check_fully_contains(pair_sections):
        p1 += 1

    if check_overlaps(pair_sections):
        p2 += 1

print("answer of puzzle 1: ", p1)
print("answer of puzzle 2: ", p2)
