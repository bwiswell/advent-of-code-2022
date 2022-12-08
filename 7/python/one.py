from typing import Any

def parse_ls (lines: list[str]) -> dict[str, Any]:
    tree = {}
    for line in lines:
        if line.startswith('dir'):
            key = line.split(' ')[1]
            tree[key] = {}
        else:
            parts = line.split(' ')
            size = int(parts[0])
            name = parts[1]
            tree[name] = size
    return tree

def set_at (tree: dict[str, Any], loc: tuple[str], val: Any):
    curr = tree
    for index in loc[:-1]:
        curr = curr[index]
    curr[loc[-1]] = val

def parse_lines (lines: list[str]) -> dict[str, Any]:
    tree = {}
    loc = ()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line == '$ cd ..':
            loc = loc[:-1]
        elif line.startswith('$ cd'):
            key = line.split(' ')[-1]
            loc = (*loc, key)
        elif line == '$ ls':
            for j in range(i + 1, len(lines) + 1, 1):
                if j == len(lines) or lines[j].startswith('$'):
                    set_at(tree, loc, parse_ls(lines[i+1:j]))
                    i = j - 1
                    break
        i += 1
    return tree

def compute_sizes (tree: dict[str, Any]) -> dict[str, Any]:
    sizes = {}
    size = 0
    for key, val in tree.items():
        if isinstance(val, int):
            sizes[key] = val
            size += val
        else:
            computed = compute_sizes(val)
            sizes[key] = computed
            size += computed['size']
    sizes['size'] = size
    return sizes
    
def find_under (sizes: dict[str, Any], loc: tuple[str], limit: int) -> list[tuple[str]]:
    under = []
    for key, val in sizes.items():
        if isinstance(val, int):
            continue
        under.extend(find_under(val, (*loc, key), limit))
        if val['size'] <= limit:
            under.append((*loc, key))
    return under

def get_size_at (tree: dict[str, Any], loc: tuple[str]) -> int:
    curr = tree
    for index in loc[:-1]:
        curr = curr[index]
    return curr[loc[-1]]['size']

def total_under (sizes: dict[str, Any], under: list[tuple[str]]) -> int:
    return sum([get_size_at(sizes, loc) for loc in under])

def open_and_find (path: str, limit: int) -> int:
    lines = [line.strip() for line in open(path).readlines()]
    tree = parse_lines(lines)
    sizes = compute_sizes(tree)
    under = find_under(sizes, (), limit)   
    return total_under(sizes, under)

print(open_and_find('7/python/input.txt', 100000))