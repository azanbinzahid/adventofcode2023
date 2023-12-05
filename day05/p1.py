def find_key(line, map):
    for k in map.keys():
        if line.startswith(k):
            return k

with open('in.txt', 'r') as f:
    seeds = []
    farm_map = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    curr_map = ""
    for line in f.readlines():
        curr_key = find_key(line, farm_map)

        if line.startswith("seeds"):
            seeds = list(map(int, line.split(":")[-1].split()))
        
        elif line.strip() == "":
            curr_map = ""

        elif curr_key:
            curr_map = curr_key
        
        else:
            dest, source, range = map(int, line.split())
            farm_map[curr_map].append(
                {
                "dest": dest, 
                 "src": source,
                "range": range
                }
            )

    # map seeds one by one
    final = []
    for seed in seeds:
        curr_seed = seed
        for m in farm_map.keys():
            curr_map = farm_map[m]
            for pair in curr_map:
                if pair['src'] <= curr_seed < (pair['src']+pair['range']):
                    curr_seed = pair['dest'] + curr_seed - pair['src'] 
                    break
            
        final.append(curr_seed)

    
    print(min(final))

        