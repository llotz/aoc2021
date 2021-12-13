import os

content = open('in.txt').read().split('\n')

coords=[]
folds=[]
for x in content:
    if '' == x:
        continue
    if 'fold' in x:
        folds.append(x.replace('fold along ', '').split('='))
        continue
    x,y=[int(y) for y in x.split(',')]
    coords.append([x,y])


for fold in folds:
    folder = int(fold[1])
    for coord in coords.copy():
        x,y=coord
        dx,dy = x,y
        if fold[0]=='y' and y>folder:
            dy=folder-(y-folder)
            if not [dx,dy] in coords:
                coords.append([dx,dy])
            coords.remove([x,y])
        elif fold[0]=='x' and x>folder:
            dx=folder-(x-folder)
            if not [dx,dy] in coords:
                coords.append([dx,dy])
            coords.remove([x,y])
xmax = max([x[0] for x in coords])
ymax = max([x[1] for x in coords])
o = ''
for y in range(ymax+1):
    for x in range(xmax+1):
        o+='X' if [x,y] in coords else ' '
    print(o)
    o=''