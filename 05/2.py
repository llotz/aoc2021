import os

l = [x for x in open('in.txt').read().split('\n')]
matrix = []
for x in range(1000):
    line = []
    for y in range(1000):
        line.append(0)
    matrix.append(line)


def heading(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def get_coordinates(line):
    left, right = line.split('->')
    left = [int(x) for x in left.split(',')]
    right = [int(x) for x in right.split(',')]
    l = min(left, right)
    r = max(left, right)
    direction = [heading(r[0]-l[0]), heading(r[1]-l[1])]
    return l, r, direction


for line in l:
    s, e, direction = get_coordinates(line)
    p = s
    while p != e:
        matrix[p[0]][p[1]] += 1
        p[0] += direction[0]
        p[1] += direction[1]
    matrix[e[0]][e[1]] += 1
o = 0
for x in matrix:
    o += sum([1 for y in x if y > 1])
print("result: "+str(o))
