digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total_cal = 0
with open('in.txt', 'r') as f:
    cal = ""
    for line in f.readlines():
        cal = ''

        for i in range(len(line)):
            if line[i].isdigit():
                cal += line[i]
                continue

            for x in digit_map:
                if x == line[i:i+len(x)]:
                    cal += str(digit_map[x])


        total_cal += int(cal[0]+cal[-1])


print(total_cal)