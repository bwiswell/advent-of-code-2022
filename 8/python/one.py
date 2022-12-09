lines = [line.strip() for line in open('8/python/input.txt').readlines()]
lines = [[int(char) for char in line] for line in lines]

visible = [[0] * len(lines[0]) for y in range(len(lines))]
for x in range(len(lines[0])):
    for y in range(len(lines)):
        height = lines[y][x]

        #Edge
        if x == 0 or y == 0 or x == len(lines[0]) - 1 or y == len(lines) - 1:
            visible[y][x] = 1
            continue

        # Above
        vis = True
        for y_p in range(0, y):
            if lines[y_p][x] >= height:
                vis = False
                break
        if vis:
            visible[y][x] = 1
            continue

        # Below
        vis = True
        for y_p in range(y + 1, len(lines)):
            if lines[y_p][x] >= height:
                vis = False
                break
        if vis:
            visible[y][x] = 1
            continue

        # Left
        vis = True
        for x_p in range(0, x):
            if lines[y][x_p] >= height:
                vis = False
                break
        if vis:
            visible[y][x] = 1
            continue

        # Right
        vis = True
        for x_p in range(x + 1, len(lines[0])):
            if lines[y][x_p] >= height:
                vis = False
                break
        if vis:
            visible[y][x] = 1
            continue


print(sum([sum(row) for row in visible]))
            