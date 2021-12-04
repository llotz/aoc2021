import os

l = [x for x in open('in.txt').read().split('\n')]
draws = [int(x) for x in l[0].split(',')]
fields = []
field_cache = []
for x in range(2, len(l)):
    if l[x] == "":
        fields.append(field_cache)
        field_cache = []
        continue
    line = [int(l[x][y:y+2]) for y in range(0, len(l[x]), 3)]
    # print(line)
    field_cache.append(line)

fields.append(field_cache)
field_cache = []

lastdraw = 0


def win(field):
    result = 0
    for line in field:
        result += sum([x for x in line if x > -1])
    print("-----")
    print(field)
    print(result*lastdraw)
    fields.remove(field)


def check_win(field):
    for line in field:
        if sum(line) == -5:
            return True
    for x in range(5):
        s = 0
        for y in range(5):
            s += field[y][x]
        if s == -5:
            return True
    return False


for draw in draws:
    lastdraw = draw
    print("draw:"+str(draw))
    for field in fields:
        for line in field:
            for f in range(len(line)):
                if line[f] == draw:
                    line[f] = -1
                    # print("found!")
    # print(fields)

    for f in fields.copy():
        if check_win(f):
            if len(fields) == 1:
                print(fields[0])
                result = 0
                for line in fields[0]:
                    result += sum([x for x in line if x > -1])
                print(result)
                print(draw)
                print(result*draw)
                exit(0)
            fields.remove(f)
