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
    
def find_over (sizes: dict[str, Any], loc: tuple[str], limit: int) -> list[tuple[str]]:
    over = []
    for key, val in sizes.items():
        if isinstance(val, int):
            continue
        over.extend(find_over(val, (*loc, key), limit))
        if val['size'] >= limit:
            over.append((*loc, key))
    return over

def get_size_at (tree: dict[str, Any], loc: tuple[str]) -> int:
    curr = tree
    for index in loc[:-1]:
        curr = curr[index]
    return curr[loc[-1]]['size']

def smallest_over (sizes: dict[str, Any], over: list[tuple[str]]) -> int:
    return min([get_size_at(sizes, loc) for loc in over])

def open_and_find (path: str) -> int:
    lines = [line.strip() for line in open(path).readlines()]
    tree = parse_lines(lines)
    sizes = compute_sizes(tree)
    needed = 30000000 - (70000000 - sizes['size'])
    over = find_over(sizes, (), needed)   
    return smallest_over(sizes, over)

print(open_and_find('7/python/input.txt'))