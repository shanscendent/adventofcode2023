import time

t1 = time.time()

with open('day05/input.txt') as f:
    seeds = f.readline()
    seeds = [int(x) for x in seeds[7:].strip().split(" ")]
    seedpairs = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
    seednumber = 0
    for pair in seedpairs:
        seednumber += pair[1]
    print(f"Warning, calculating seed locations {seednumber} times!")
    f.readline()
    lines = f.readlines()
    maps = []
    mapnames = []
    seedmap = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "map:" in line:
            maps.append(seedmap)
            mapnames.append(line.split(" map:")[0])
            seedmap = []
            continue
        seedmap.append([int(x) for x in line.split(" ")])
    maps.append(seedmap)
    mapnames.append(line.split(" map:")[0])

def location(seed):
    i = -2
    source = seed
    dest = seed
    for map in maps:
        i += 1
        if not map:
            continue
        for line in map:
            if source in range(line[1], line[1] + line[2]):
                dest = source - line[1] + line[0]
            else:
                pass
        source = dest
    return dest

minimum = float('inf')

n = 0
for seedpair in seedpairs:
    n += 1
    print(f"Working on seedpair {seedpair}, {n}/{len(seedpair)}")
    for seed in range(seedpair[0], seedpair[0] + seedpair[1]):
        minimum = min(minimum, location(seed))

print(f"Lowest location number: {minimum}")

t2 = time.time()
print(t2-t1)
