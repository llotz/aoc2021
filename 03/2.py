import os

epsilon = ""
gamma = ""
l = [x for x in open('in.txt').read().split('\n')]
e = l.copy()
g = l.copy()
for x in range(len(l[0])):
    a = []
    for z in l:
        a.append(int(z[x]))
    if sum(a) > len(l)/2:
        epsilon += "0"
        gamma += "1"
    else:
        epsilon += "1"
        gamma += "0"

print("epsilon:"+epsilon)
for x in range(len(l[0])):
    print(e)
    print(epsilon[x])
    if(len(e) == 1):
        break
    for y in e.copy():
        if y[x] != epsilon[x]:
            print("kick:"+y)
            e.remove(y)

print("gamma:"+gamma)
for x in range(len(l[0])):
    if(len(g) == 1):
        break
    for y in g.copy():
        if y[x] != gamma[x]:
            g.remove(y)

print(str(int(g[0], 2)))
print(str(int(e[0], 2)))
print(int(e[0], 2)*int(g[0], 2))
