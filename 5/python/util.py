def parse_instruction (instruction: str) -> tuple[int, int, int]:
    line = instruction.strip()[5:].replace(' from ', '-').replace(' to ', '-')
    parts = [int(p) for p in line.split('-')]
    return tuple(parts)

def parse_instructions (instructions: list[str]) -> list[tuple[int, int, int]]:
    return [parse_instruction(i) for i in instructions]

def parse_drawing (lines: list[str]) -> list[list[str]]:
    n = max([int(i) for i in lines.pop().strip().split('   ')])
    stacks = [[] for _ in range(n)]
    for line in lines:
        for s, i in enumerate(range(0, len(line), 4)):
            if line[i+1] != ' ':
                stacks[s].append(line[i+1])
    return stacks

def parse_input (inputs: list[str]) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    idx = min([i for i in range(len(inputs)) if inputs[i] == '\n'])
    stacks = parse_drawing(inputs[:idx])
    instructions = parse_instructions(inputs[idx+1:])
    return stacks, instructions

def make_move (stacks: list[list[str]], instruction: tuple[int, int, int], ordered: bool) -> list[list[str]]:
    count = instruction[0]
    location = instruction[1] - 1
    destination = instruction[2] - 1
    if not ordered:
        for _ in range(count):
            stacks[destination].insert(0, stacks[location].pop(0))
    else:
        for i in range(count - 1, -1, -1):
            stacks[destination].insert(0, stacks[location].pop(i))
    return stacks