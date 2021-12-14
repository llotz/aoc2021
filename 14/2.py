import os

l = [int(x) for x in open('in.txt').read().split('\n')]
o = 0
for x in range(3, len(l)):
    if((l[x-1]+l[x-2]+l[x-3]) < (l[x]+l[x-1]+l[x-2])):
        o += 1
print(o)
