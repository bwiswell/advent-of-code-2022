lines = [line.strip() for line in open('8/python/input.txt').readlines()]
lines = [[int(char) for char in line] for line in lines]

scenic = [[1] * len(lines[0]) for y in range(len(lines))]
for x in range(len(lines[0])):
    for y in range(len(lines)):
        height = lines[y][x]

        # Above
        trees = 0
        for y_p in range(y - 1, -1, -1):
            trees += 1
            if lines[y_p][x] >= height:
                break
        scenic[y][x] *= trees

        # Below
        trees = 0
        for y_p in range(y + 1, len(lines)):
            trees += 1
            if lines[y_p][x] >= height:
                break
        scenic[y][x] *= trees

        # Left
        trees = 0
        for x_p in range(x - 1, -1, -1):
            trees += 1
            if lines[y][x_p] >= height:
                break
        scenic[y][x] *= trees

        # Right
        trees = 0
        for x_p in range(x + 1, len(lines[0])):
            trees += 1
            if lines[y][x_p] >= height:
                break
        scenic[y][x] *= trees


print(max([max(row) for row in scenic]))
            