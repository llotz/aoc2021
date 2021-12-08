import os

l = [x for x in open('in.txt').read().split('\n')]
o = []


def createTable(input):
    sol = {}
    num = {}
    for y in input:
        if len(y) == 2:
            sol[y] = "1"
            num[1] = y
        if len(y) == 3:
            sol[y] = "7"
            num[7] = y
        if len(y) == 4:
            sol[y] = "4"
            num[4] = y
        if len(y) == 7:
            sol[y] = "8"
            num[8] = y

    fiver = [x for x in input if len(x) == 5]
    sixer = [x for x in input if len(x) == 6]
    for x in fiver:
        a, b = num[1]
        if a in x and b in x:
            sol[x] = "3"
            num[3] = x
    fiver.remove(num[3])

    for x in sixer:
        sum = 0
        for c in x:
            if c in num[3]:
                sum += 1
        if sum == 5:
            sol[x] = "9"
            num[9] = x
    sixer.remove(num[9])

    return sol

    # for y in input:
    # if len(y) == 5: # possible: 5,2

    # if len(y) == 6: #possible: 6,0

    # o.append(int(l))


for x in l:
    l = []
    input, output = x.split('|')
    input = input.split()
    output = output.split()
    print(createTable(input))


print(sum(o))
