elfs = []
with open('input.txt', 'r') as file:
    elf = []
    for line in file:
        if len(line.rstrip()) == 0:
            elfs.append(sum(elf))
            elf = []
        else:
            elf.append(int(line))
    elfs.append(sum(elf))
elfs.sort(reverse=True)

print(f'Top elf: {elfs[0]}')
print(f'Top elfs: {sum(elfs[:3])}')