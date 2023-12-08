from math import lcm

with open('in.txt', 'r') as f:

    first = 0
    dir_map = {}
    lines = f.readlines()
    start = []
    
    instructions = list(lines[0].strip())
    for line in lines[2:]:
        src, dir = line.split(' = ')
        left, right = dir[1:9].split(', ')
        dir_map[src] = {
            'L': left,
            'R': right,
        }

        if src[-1] == 'A':
            start.append(src)

    all_path_len = []
    for s in start:
        curr = s
        path = 0
        while curr[-1] != 'Z':
            for i in instructions:
                curr = dir_map[curr][i]
                path += 1
                if curr[-1] == 'Z':
                    break

        all_path_len.append(path)

    print(lcm(*all_path_len))
