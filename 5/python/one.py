from util import *

lines = open('5/python/input.txt').readlines()
stacks, instructions = parse_input(lines)
for instruction in instructions:
    stacks = make_move(stacks, instruction, False)

output = [stack[0] for stack in stacks]
print(''.join(output))