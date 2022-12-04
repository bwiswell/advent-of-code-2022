def priority (char: str) -> int:
    uni = ord(char)
    return uni - 96 if uni > 90 else uni - 38
    
lines = open('three/python/input.txt').readlines()
total = 0
for line in lines:
    clean = line.strip()
    n = len(clean) // 2
    first, second = clean[:n], clean[n:]
    for char in first:
        if char in second: 
            total += priority(char)
            break
        
print(f'Total: {total}')