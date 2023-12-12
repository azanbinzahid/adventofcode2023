import math


springs = []
arrangements = []

with open('in.txt', 'r') as f:
    for line in f.readlines():
        s, arr = line.strip().split()
        springs.append(s)
        arrangements.append(list(map(int, arr.split(","))))
    

def dp(spring, arrangement):
    if arrangement == []:
        if spring == '':
            return 1
        else:
            if '#' not in spring:
                return 1
            else:
                return 0
    

    elif spring == '':
        return 0
    
    elif spring[0] == '.':
        return dp(spring[1:], arrangement)
    
    elif spring[0] == '#':
            group_size = arrangement[0]
            if len(spring) >= group_size and '.' not in spring[:group_size]:
                new_spring = spring[group_size:]
                new_arrangement = arrangement[1:]
                if len(new_spring) > 0:
                    if new_spring[0] in ['.', '?']:
                        return dp(new_spring[1:], new_arrangement)
                    else:
                        return 0
                else:
                    return dp(new_spring, new_arrangement)
            else:
                return 0

    elif spring[0] == '?':
        ans = 0

        ans += dp(spring[1:], arrangement.copy())
        group_size = arrangement[0]
        if len(spring) >= group_size and '.' not in spring[:group_size]:
            new_spring = spring[group_size:]
            new_arrangement = arrangement[1:]
            if len(new_spring) > 0:
                if new_spring[0] in ['.', '?']:
                    ans += dp(new_spring[1:], new_arrangement)
            else:
                ans +=  dp(new_spring, new_arrangement)
        
        return ans

    else:
        return print("Error in input")





ways = []
for i in range(len(springs)):
    ways.append(dp(springs[i], arrangements[i]))
    # print(ways)
    # break

print(sum(ways))

