#https://open.kattis.com/problems/parking2
def calc(arr):
	for i in range(len(arr)):
		arr[i] = int(arr[i])
	return(2*(max(arr)-min(arr)))
uh = int(input())
out = []
for i in range(uh):
	input()
	out += [calc(input().split())]
for thing in out:
	print(thing)
