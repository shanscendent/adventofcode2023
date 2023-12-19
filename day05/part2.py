import time
from multiprocessing import Pool
from itertools import chain
from datetime import timedelta

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

seedchain = iter([])
for seedpair in seedpairs:
    seedchain = chain(seedchain, range(seedpair[0], seedpair[0] + seedpair[1]))

print(seedchain)

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
    # print(f"Trying to minimize {dest}")
    return dest

with Pool(16) as p:
    locationiterator = p.imap_unordered(location, seedchain)
    
    minimum = float('inf')

    n = 0
    for l in locationiterator:
        n += 1
        if n % 50000 == 0:
            buffer = len(locationiterator._items)
            percent = n/seednumber*100
            elapsed = round(time.time()-t1)
            remaining = elapsed * (1/percent - 1)
            print(f"{n}/{seednumber} ({percent:0.2f}%), buf: {buffer}, ", end="")
            print(f"elapsed: {str(timedelta(seconds=elapsed))}, remaining: {str(timedelta(seconds=remaining))}")
        minimum = min(minimum, l)

print(f"Lowest location number: {minimum}")

t2 = time.time()
print(t2-t1)
