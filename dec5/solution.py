from collections import deque
import re

fhand = open("input.txt")

stacks_p1 = []
stacks_p2 = []
for i in range(9):
    stacks_p1.append(deque())
    stacks_p2.append(deque())


def move_stack_one(to_move, move_from, move_to):
    for _ in range(to_move):
        popped = stacks_p1[move_from].pop()
        stacks_p1[move_to].append(popped)

def move_stack_two(to_move, move_from, move_to):
    popped = deque()
    for _ in range(to_move):
        popped.appendleft(stacks_p2[move_from].pop())

    for _ in range(to_move):
        p = popped.popleft()
        stacks_p2[move_to].append(p)


for line in fhand:
    if "[" in line:
        match = re.finditer("\[.\]", line)
        for m in match:
            string = m.group().replace("[", "").replace("]", "")
            string_idx = int(m.start() / 4)
            stacks_p1[string_idx].appendleft(string)
            stacks_p2[string_idx].appendleft(string)
    elif "move" in line:
        a, b, c = re.findall("\d+", line)

        to_move = int(a)
        move_from = int(b) - 1
        move_to = int(c) - 1

        move_stack_one(to_move,move_from,move_to)
        move_stack_two(to_move, move_from, move_to)
    else:
        pass

p2 = ""
p1 =  ""
for i in range(9):
    p1 += stacks_p1[i][len(stacks_p1[i]) - 1]
    p2 += stacks_p2[i][len(stacks_p2[i]) - 1]

print("Answer for puzzle 1: ",p1)
print("Answer for puzzle 2: ",p2)
