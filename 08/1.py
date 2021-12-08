import os

l = [x for x in open('in.txt').read().split('\n')]
o = 0
for x in l:
    last = x.split('|')[1].split()
    for y in last:
        if len(y) in [2, 3, 4, 7]:
            o += 1
print(o)
