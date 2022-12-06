fhand = open("input.txt")


def lz_string_val(lz_reader):
    """
    Returns the current value of the string in the lazy stream reader
    """
    return lz_reader[0]


def lz_string_index(lz_reader):
    """
    Returns the current index the lazy stream reader is on
    """
    return lz_reader[1]


def lz_string_rest(lz_reader):
    """
    Return the rest of the lazy stream reader
    """
    return lz_reader[2]()


def lz_string_reader(idx, string):
    """
    Creates a lazy stream reader for the string
    """
    return [string[idx], idx, lambda: lz_string_reader(idx + 1, string)]


def find_first_distinct(string, distinct_no):
    """
    Finds the marker for the puzzle
    """
    stream = lz_string_reader(0, string)

    read_strings = ""

    while True:

        current_val = lz_string_val(stream)

        if current_val not in read_strings:
            read_strings += current_val
        else:
            current_val_in = read_strings.index(current_val)
            read_strings = read_strings[current_val_in + 1 :] + current_val

        if len(read_strings) == distinct_no:
            return lz_string_index(stream) + 1

        stream = lz_string_rest(stream)


input_string = ""

for line in fhand:
    input_string += line.strip()

print("Answer of puzzle 1 ", find_first_distinct(input_string, 4))
print("Answer of puzzle 2", find_first_distinct(input_string, 14))
