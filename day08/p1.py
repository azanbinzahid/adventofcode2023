with open('in.txt', 'r') as f:

    first = 0
    dir_map = {}
    lines = f.readlines()
    
    instructions = list(lines[0].strip())
    for line in lines[2:]:
        src, dir = line.split(' = ')
        left, right = dir[1:9].split(', ')
        dir_map[src] = {
            'L': left,
            'R': right,
        }

    
    curr = 'AAA'
    end = 'ZZZ'
    path = []
    while curr != end:
        for i in instructions:
            curr = dir_map[curr][i]
            path.append(curr)
            if curr == end:
                break

    print(len(path))
    # print(dir_map)
