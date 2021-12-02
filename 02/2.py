import os

pos = 0
depth = 0
aim = 0

l = [x for x in open('in.txt').read().split('\n')]
for x in l:
    f = x.split()
    if f[0][0] == 'f':
        pos += int(f[1])
        depth += aim*int(f[1])
    elif f[0][0] == 'd':
        aim += int(f[1])
    else:
        aim -= int(f[1])
print(pos*depth)
