def read(filename='in.txt'):
    data1 = []
    data2 = []
    with open(filename, 'r') as f:
        data = data1
        for line in f.readlines():
            if line.strip() == '':
                data = data2
                continue
            data.append(line.strip())

    return data1, data2
    


def register(workflows):
    data = {}

    for w in workflows:
        name, rules = w.split('{')
        data[name] = []
        for r in rules[:-1].split(','):
            if ':' not in r:
                    data[name].append({
                    'condition': None,
                     'rule': r
                    })
            else:
                condition, rule = r.split(':')
                variable, operator, value = condition[0], condition[1], int(condition[2:])
                data[name].append({
                    'condition': (variable, operator, value),
                     'rule': rule
                    })

    return data



def extract(parts):
    data = []
    for p in parts:
        part = {}
        x, m, a, s =  map(lambda l:int(l.split('=')[1]), p[1:-1].split(','))
        part = {
            'x': x,
            'a': a,
            's': s,
            'm': m,
        }
        data.append(part)
    return data


def run(workflow_name, part):
    # print(workflow_name)
    workflow = workflows[workflow_name]
    for step in workflow:
        rule = step['rule']
        condition = step['condition']

        if condition is None:
            if rule in ['A', 'R']:
                return rule
            else:
                return run(rule, part)

        else:
            variable, operator, value = condition
            if (operator == '>' and part[variable] > value) \
                or (operator == '<' and part[variable] < value):
                if rule in ['A', 'R']:
                    return rule
                else:
                    return run(rule, part)
            else:
                continue


def solve(parts):
    ans = 0
    for p in parts:
        if run('in', p) == 'A':
            ans += sum(p.values())

    print(ans)

if __name__ == "__main__":

    workflows, parts = read()
    # print(workflows)
    workflows = register(workflows)
    parts = extract(parts)

    # for w in workflows:
    #     print(w)
    #     for step in workflows[w]:
    #         print(step)

    # print('')
    # print(parts)
    solve(parts)
