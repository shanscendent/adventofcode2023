import time
import re

t1 = time.time()

elves = []

with open('day01/input.txt') as f:
    lines = f.readlines()
    total = 0
    for value in lines:
        temp = re.findall(r'\d', value)
        total += int(''.join([temp[0], temp[-1]]))

print(total)

t2 = time.time()
print(t2-t1)
