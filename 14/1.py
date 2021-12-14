import os

l = [x for x in open('test_in.txt').read().split('\n')]
str = l[0]
for x in l[1:]:
	print(x)