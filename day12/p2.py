import math


springs = []
arrangements = []
memo = {}

with open('in.txt', 'r') as f:
    for line in f.readlines():
        s, arr = line.strip().split()
        arr = list(map(int, arr.split(",")))


        arrx5 = []
        sx5 = []
        for i in range(5):
            sx5.append(s)
            arrx5.extend(arr)
        

        springs.append("?".join(sx5))
        arrangements.append(arrx5)

    

def dp(spring, arrangement):
    spring = spring.strip(".")

    # memoization
    if (spring, tuple(arrangement)) in memo:
        return memo[(spring, tuple(arrangement))]


    if arrangement == []:
        if spring == '' or  '#' not in spring:
            return 1
        else:
            return 0    

    elif spring == '':
        return 0
        
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

        if (spring, tuple(arrangement)) not in memo:
            memo[(spring, tuple(arrangement))] = ans
        
        return ans

    else:
        return print("Error in input")





ways = []
for i in range(len(springs)):
    ways.append(dp(springs[i], arrangements[i]))
    # print(ways)
    # break

print(sum(ways))
