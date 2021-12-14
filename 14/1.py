import os
import re
from collections import Counter

l = [x for x in open('test_in.txt').read().split('\n')]
str = l[0]
for f in range(10):
	for x in l[2:]:
		strarr=[p for p in str]
		m=x.split(',')
		g=[o.start() for o in re.finditer(m[0],str)]
		for i in g:
			strarr.insert(i+1,m[1])
		str="".join(strarr)
print(Counter(str))