import os

l = [x for x in open('in.txt').read().split('\n')]
matrix = []
for x in range(1000):
    line = []
    for y in range(1000):
        line.append(0)
    matrix.append(line)


def get_coordinates(line):
    left, right = line.split('->')
    left = [int(x) for x in left.split(',')]
    right = [int(x) for x in right.split(',')]
    l = min(left, right)
    r = max(left, right)
    return l, r


for line in l:
    s, e = get_coordinates(line)
    #print(s, e)
    if s[0] != e[0] and s[1] != e[1]:
        # print("nope")
        continue
    for yy in range(s[0], e[0]+1):
        for xx in range(s[1], e[1]+1):
            # if yy == xx or yy+xx == s[1]+e[1]:
            matrix[xx][yy] = matrix[xx][yy]+1
    # for x in matrix:
 #   print(x)
o = 0
for x in matrix:
    o += sum([1 for y in x if y > 1])
print("result: "+str(o))
