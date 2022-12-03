MAPPING = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

lines = open('two/python/input.txt').readlines()
moves = [(MAPPING[line[0]], MAPPING[line[2]]) for line in lines]

score = 0
for k, v in moves:
    if v == k:
        score += v + 4
    elif (v - k == 1) or (v - k == -2):
        score += v + 7
    else:
        score += v + 1

print(f'Overall score: {score}')
print(score)
