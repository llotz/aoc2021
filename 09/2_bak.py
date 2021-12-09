import os

l = [x for x in open('in.txt').read().split('\n')]
grid = []
basin = []


def get_higher_neighbours(x, y):
    n = []
    s = 0
    v = int(grid[y][x])
    s += 1
    if x > 0 and int(grid[y][x-1]) > v and int(grid[y][x-1]) != 9:
        s += get_higher_neighbours(x-1, y)
    if y > 0 and int(grid[y-1][x]) > v and int(grid[y-1][x]) != 9:
        s += get_higher_neighbours(x, y-1)
    if y+1 < len(grid) and int(grid[y+1][x]) > v and int(grid[y+1][x]) != 9:
        s += get_higher_neighbours(x, y+1)
    if x+1 < len(l[0]) and int(grid[y][x+1]) > v and int(grid[y][x+1]) != 9:
        s += get_higher_neighbours(x+1, y)
    return s


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
            print(get_higher_neighbours(x, y))
