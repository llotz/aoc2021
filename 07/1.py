import os
import math

l = [int(x) for x in open('in.txt').read().split(',')]
l = sorted(l)

least = 0
for x in range(max(l)):
    s = 0
    for p in l:
        m = abs(p-x)
        s += m*(m+1)/2
    if least == 0 or least > s:
        least = s
    print(x)
print(least)
