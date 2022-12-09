def translate_line (line: str) -> list[tuple[int, int]]:
    direction, amount = line.strip().split()
    amount = int(amount)
    if direction == 'R':
        return [(1, 0)] * amount
    elif direction == 'L':
        return [(-1, 0)] * amount
    elif direction == 'U':
        return [(0, -1)] * amount
    else:
        return [(0, 1)] * amount

def translate (lines: list[str]) -> list[tuple[int, int]]:
    translation = []
    for line in lines:
        translation.extend(translate_line(line))
    return translation

def adjacent (a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

def move_tail (head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    if head[0] == tail[0]:
        if head[1] < tail[1]:
            return tail[0], tail[1] - 1
        else:
            return tail[0], tail[1] + 1
    elif head[1] == tail[1]:
        if head[0] < tail[0]:
            return tail[0] - 1, tail[1]
        else:
            return tail[0] + 1, tail[1]
    else:
        if head[0] < tail[0]:
            if head[1] < tail[1]:
                return tail[0] - 1, tail[1] - 1
            else:
                return tail[0] - 1, tail[1] + 1
        else:
            if head[1] < tail[1]:
                return tail[0] + 1, tail[1] - 1
            else:
                return tail[0] + 1, tail[1] + 1

def simulate (lines: list[tuple[int, int]]) -> int:
    visited = set()
    head = 0, 0
    tail = 0, 0
    for line in lines:
        dx, dy = line
        head = head[0] + dx, head[1] + dy
        if not adjacent(head, tail):
            tail = move_tail(head, tail)
        visited.add(tail)
    return len(visited)




lines = open('9/python/input.txt').readlines()
lines = translate(lines)
print(simulate(lines))

