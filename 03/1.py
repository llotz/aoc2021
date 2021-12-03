import os

epsilon = ""
gamma = ""

l = [x for x in open('in.txt').read().split('\n')]

for x in range(len(l[0])):
    a = []
    for z in l:
        a.append(int(z[x]))
    print(a)
    if sum(a) > len(l)/2:
        epsilon += "0"
        gamma += "1"
    else:
        gamma += "0"
        epsilon += "1"
print(gamma+"-"+epsilon)
print(int(epsilon, 2)*int(gamma, 2))
