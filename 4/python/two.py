lines = open('4/rockstar/input.txt')

total = 0
for line in lines:
    subjs = line.strip().split(',')
    min_a, max_a = subjs[0].split('-')
    min_b, max_b = subjs[1].split('-')
    min_a, max_a, min_b, max_b = int(min_a), int(max_a), int(min_b), int(max_b)

    if min_a <= min_b and max_a >= min_b:
        total += 1
    elif min_b <= min_a and max_b >= min_a:
        total += 1

print(total)