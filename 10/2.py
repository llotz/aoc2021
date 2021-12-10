import os
opener=['(', '{', '[', '<']
closer=[')', '}', ']', '>']

opens=[]

values={
	')':1,
	']':2,
	'}':3,
	'>':4
}
result=[]
lines = open('in.txt').read().split('\n')
corrupted=[]
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
				corrupted.append(line)
				break
for x in corrupted:
	lines.remove(x);

for line in lines:
	tempScore=0
	opens=[]
	for c in line:
		if c in opener:
			opens.append(c)
		elif c in closer:
			if opens[-1]==opener[closer.index(c)]:
				opens.pop()
	for x in reversed(opens):
		tempScore=tempScore*5+values[closer[opener.index(x)]]
	result.append(tempScore)
result.sort()
print(result[int(len(result)/2)])