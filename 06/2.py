import os

fishes = [int(x) for x in open('in.txt').read().split(',')]

types = dict.fromkeys(range(0, 9))
for x in range(0, 9):
    types[x] = 0
clean = types.copy()
for x in fishes:
    types[x] += 1
print(types)

for day in range(256):
    temp = clean.copy()
    for x, count in types.items():
        if x == 0:
            temp[6] += count
            temp[8] += count
        else:
            temp[x-1] += count
    types = temp
print(types)
print(sum(types.values()))
