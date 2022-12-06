def all_neq (chars: list[str]) -> bool:
    return len(set(chars)) == len(chars)

def find_marker (signal: str) -> int:
    for i in range(0, len(signal) - 4, 1):
        if all_neq(signal[i:i+4]):
            return i + 4

print(find_marker(open('6/python/input.txt').readline().strip()))