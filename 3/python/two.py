def priority (char: str) -> int:
    uni = ord(char)
    return uni - 96 if uni > 90 else uni - 38
    
lines = open('three/python/input.txt').readlines()
total = 0
for i in range(0, len(lines), 3):
    a = lines[i].strip()
    b = lines[i + 1].strip()
    c = lines[i + 2].strip()
    cands = []
    for char in a:
        if char in b: cands.append(char)
    for char in cands:
        if char in c:
            total += priority(char)
            break
        
print(f'Total: {total}')