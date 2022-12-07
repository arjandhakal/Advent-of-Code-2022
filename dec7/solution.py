import re


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.dirs = None
        self.files = None
        self.parent = parent

    def add_file(self, file):
        if self.files == None:
            self.files = [file]
        else:
            self.files.append(file)
        return file

    def fetch_parent(self):
        return self.parent

    def add_directory(self, dir):
        if self.dirs == None:
            self.dirs = [dir]
        else:
            self.dirs.append(dir)
        return dir


def find_dir(name, dir):
    """
    Returns the directory with the given name in current directory if found,
    otherwise returns None
    """
    if dir.dirs == None:
        return None
    else:
        search_dir = [x for x in dir.dirs if x.name == name]
        if len(search_dir) == 0:
            return None
        else:
            return search_dir[0]


def calculate_dir_size(dir):
    """
    Calculates the total size of a directory
    """
    current_dir_files_size = 0
    if dir.files != None:
        current_dir_files_size += sum([x.size for x in dir.files])
    current_dir_sub_dir_size = 0
    if dir.dirs != None:
        current_dir_sub_dir_size += sum([calculate_dir_size(x) for x in dir.dirs])
    total_size = current_dir_files_size + current_dir_sub_dir_size
    return total_size


fhand = open("input.txt")

root_dir = Directory("/")

current_dir = root_dir


for line in fhand:
    line = line.strip()
    if "$ cd" in line:
        search = re.search("(?<=cd\s).*", line)
        dir_name = line[search.start() : search.end()]
        if dir_name == "..":
            current_dir = current_dir.parent
        elif dir_name == "/":
            current_dir = root_dir
        else:
            line_dir = find_dir(dir_name, current_dir)
            if line_dir != None:
                current_dir = line_dir
            else:
                new_dir = Directory(dir_name, current_dir)
                current_dir.add_directory(new_dir)
                current_dir = new_dir
    elif "$ ls" in line:
        continue
    elif re.match("dir ", line):
        search = re.search("(?<=dir\s).*", line)
        dir_name = line[search.start() : search.end()]
        line_dir = find_dir(dir_name, current_dir)
        if line_dir == None:
            current_dir.add_directory(Directory(dir_name, current_dir))
    else:
        file_size, file_name = line.split(" ")
        new_file = File(file_name, int(file_size))
        current_dir.add_file(new_file)


p1 = []


def puzzle_one_answer(dir):
    current_dir_size = calculate_dir_size(dir)

    if current_dir_size <= 100_000:
        p1.append(current_dir_size)

    sub_dirs = dir.dirs

    if sub_dirs:
        for d in sub_dirs:
            puzzle_one_answer(d)


puzzle_one_answer(root_dir)
print("Answer for puzzle 1", sum([x for x in p1]))

p2 = []


def puzzle_two_answer(dir, min_size):
    current_dir_size = calculate_dir_size(dir)
    if current_dir_size >= min_size:
        p2.append(current_dir_size)

    sub_dirs = dir.dirs

    if sub_dirs:
        for d in sub_dirs:
            puzzle_two_answer(d, min_size)


total_size_occupied = calculate_dir_size(root_dir)
total_space_available = 70000000
total_space_needed = 30000000
current_free = total_space_available - total_size_occupied
clean_up_space = total_space_needed - current_free


puzzle_two_answer(root_dir, clean_up_space)
p2 = sorted(p2)
print("Answer for puzzle 2: ", p2[0])
