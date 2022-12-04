MAPPING = { 'A': 0, 'B': 1, 'C': 2, 'X': -1, 'Y': 0, 'Z': 1 }
lines = open('two/python/input.txt').readlines()
moves = [(MAPPING[line[0]], MAPPING[line[2]]) for line in lines]
print(f'New score: {sum([(k + v) % 3 + 1 + (v + 1) * 3 for k, v in moves])}')