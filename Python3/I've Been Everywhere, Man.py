#https://open.kattis.com/problems/everywhere
n = int(input())
out = []
for i in range(n):
	temp = []
	for i in range(int(input())):
		temp += [input()]
	out += [len(list(set(temp)))]
for i in range(n):
	print(out[i])
