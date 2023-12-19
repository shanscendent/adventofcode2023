import time

t1 = time.time()

with open('day05/input.txt') as f:
    seeds = f.readline()
    seeds = [int(x) for x in seeds[7:].strip().split(" ")]
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

locations = []
for seed in seeds:
    print(f"Trying seed {seed}.")
    i = -2
    source = seed
    dest = seed
    for map in maps:
        i += 1
        if not map:
            continue
        print(f"Trying {mapnames[i]} map: ", end="")
        for line in map:
            if source in range(line[1], line[1] + line[2]):
                dest = source - line[1] + line[0]
            else:
                pass
        source = dest
        print(f"Source {source} in line {line} corresponds to dest {dest}")
    locations.append(dest)
    print(f"Location for seed {seed} is location {dest}")

# print(locations)
print(f"Lowest location number: {min(locations)}")

t2 = time.time()
print(t2-t1)
