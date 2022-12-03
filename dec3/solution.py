fhand = open("input.txt")


def priority_lowercase(order):
    """
    Changes the value of lowercase letter obtained through ord to 1 - 26
    """
    return order - 96


def priority_uppercase(order):
    """
    Changes the value of lowercase letter obtained through ord to 27 - 52
    """
    return order - 38


def get_first_half(str):
    """
    Returns the first half of a string
    """
    return str[: len(str) // 2]


def get_second_half(str):
    """
    Returns the second half of a string
    """
    return str[len(str) // 2 :]


def get_string_hashmap(str):
    """
    Changes the string value to a hashmap
    example: "abc" -> {a : True, b: True, c: True}
    """
    output = dict()
    for s in str:
        output[s] = True
    return output


def find_common_string(hashmap, str):
    """
    From the letters in string, finds the first matching key
    """
    for s in str:
        if hashmap.get(s, False):
            return s


def find_common_str2(hashmap1, hashamp2, hashmap3):
    """
    From three hashmap, finds the common key between them all
    """
    for key in hashmap1.keys():
        if hashamp2.get(key, False) and hashmap3.get(key, False):
            return key


puzzle_one = 0


puzzle_two = 0
all_group = []
current_group = []

for line in fhand:
    first_compartment = get_first_half(line)
    second_compartment = get_second_half(line)

    first_compartment_hashmap = get_string_hashmap(first_compartment)

    common_item = find_common_string(first_compartment_hashmap, second_compartment)

    common_item_order = ord(common_item)

    if common_item_order >= 97 and common_item_order <= 122:
        puzzle_one += priority_lowercase(common_item_order)
    else:
        puzzle_one += priority_uppercase(common_item_order)

    # for puzzle 2
    current_group.append(line)
    if len(current_group) == 3:
        all_group.append(current_group)
        current_group = []


for group in all_group:
    h1 = get_string_hashmap(group[0])
    h2 = get_string_hashmap(group[1])
    h3 = get_string_hashmap(group[2])

    common_item_order = ord(find_common_str2(h1, h2, h3))

    if common_item_order >= 97 and common_item_order <= 122:
        puzzle_two += priority_lowercase(common_item_order)
    else:
        puzzle_two += priority_uppercase(common_item_order)


print("answer of first puzzle: ", puzzle_one)
print("answer of second puzzle", puzzle_two)
