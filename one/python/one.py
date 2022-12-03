elfs = []
with open('one/python/input.txt', 'r') as file:
    elf = 0
    for line in file:
        if len(line.rstrip()) == 0:
            elfs.append(elf)
            elf = 0
        else:
            elf += int(line)
    elfs.append(elf)
elfs.sort(reverse=True)

print(f'Top elf: {elfs[0]}')
print(f'Top elfs: {sum(elfs[:3])}')