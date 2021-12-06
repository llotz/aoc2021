import os

fishes = [int(x) for x in open('in.txt').read().split(',')]
for x in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1
print(len(fishes))
