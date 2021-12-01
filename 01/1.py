import os

l = [int(x) for x in open('in.txt').read().split('\n')]
o = 0
for x in range(1, len(l)):
    if(l[x-1] < l[x]):
        o += 1
print(o)
