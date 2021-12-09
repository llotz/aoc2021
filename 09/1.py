import os

l = [x for x in open('in.txt').read().split('\n')]
grid = []
o = 0
for x in l:
    grid.append([y for y in x])
for y in range(len(grid)):
    for x in range(len(l[0])):
        neighbours = []
        # print(grid[y][x])
        if x > 0:
            neighbours.append(int(grid[y][x-1]))
        if y > 0:
            neighbours.append(int(grid[y-1][x]))
        if y+1 < len(grid):
            neighbours.append(int(grid[y+1][x]))
        if x+1 < len(l[0]):
            neighbours.append(int(grid[y][x+1]))
        deepest = True
        for j in neighbours:
            if j <= int(grid[y][x]):
                deepest = False
        if deepest:
            o += int(grid[y][x])+1
print(o)
