#https://open.kattis.com/problems/helpaphd
def calc(prob):
	if "=" in prob[0]:
		return("skipped")
	else:
		return(int(prob[0]) + int(prob[1]))
n = int(input())
out = []
for i in range(n):
	out += [calc(input().split("+"))]
for thing in out:
	print(thing)
