import math

with open('in.txt', 'r') as f:
    data = f.readlines()
    time = [int("".join(list(data[0].split(":")[-1].split())))]
    distance = [int("".join(list(data[1].split(":")[-1].split())))]

    def get_final_distance(speed, time):
        return speed * time
    
    records = []
    for id, t in enumerate(time):
        count = 0
        for i in range(t):
            if get_final_distance(t-i, i) > distance[id]:
                count+=1
        records.append(count)
    
    print(math.prod(records))