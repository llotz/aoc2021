import os
opener=['(', '{', '[', '<']
closer=[')', '}', ']', '>']

opens=[]
fails=[]

values={
	')':3,
	']':57,
	'}':1197,
	'>':25137
}

lines = open('in.txt').read().split('\n')

for line in lines:
	opens=[]
	for c in line:
		if c in opener:
			opens.append(c)
		elif c in closer:
			if opens[-1]==opener[closer.index(c)]:
				opens.pop()
			else:
				print(opens[-1], c)
				fails.append(c)
				break
print(fails)
print(sum([values[x] for x in fails]))