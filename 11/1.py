import os

matrix = []
explosions = 0


def define_boundaries(x):
    min, max = 0, 0
    if x > 0:
        min = x-1
    if x < 9:
        max = x+1
    else:
        max = 9
    return min, max


def check_matrix(matrix):
    exploders = []  # detonations are way cooler than flashes
    for y in range(10):
        for x in range(10):
            if(matrix[y][x] > 9):
                exploders.append([x, y])
    return exploders


def add_one():
    for y in range(10):
        for x in range(10):
            matrix[y][x] += 1


def explode(exploders):
    for m in exploders:
        x, y = m[0], m[1]
        xmin, xmax = define_boundaries(x)
        ymin, ymax = define_boundaries(y)
        for dx in range(xmin, xmax):
            for dy in range(ymin, ymax):
                matrix[dy][dx] += 1
        matrix[y][x] = 0
        print(x, y, "xmin/max:", xmin, xmax, "ymin/max", ymin, ymax)


l = [x for x in open('test_in.txt').read().split('\n')]


for x in l:
    line = []
    for y in x:
        line.append(int(y))
    matrix.append(line)

for x in range(100):
    add_one()
    exploders = check_matrix(matrix)
    while exploders != []:
        explosions += len(exploders)
        explode(exploders)
        exploders = check_matrix(matrix)
print(explosions)
