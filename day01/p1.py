total_cal = 0
with open('sample.txt', 'r') as f:
    cal = ""
    for line in f.readlines():
        
        cal = ''
        for value in line:
            cal += value if value.isdigit() else ''

        total_cal += int(cal[0]+cal[-1])


print(total_cal)