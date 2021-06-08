#https://open.kattis.com/problems/numberfun
def calc(arr):
	for i in range(len(arr)):
		arr[i] = int(arr[i])
	ispos = False
	if arr[0] + arr[1] == arr[2]:
		ispos = ispos or True
	elif arr[0] - arr[1] == arr[2]:
		ispos = ispos or True
	elif arr[1] - arr[0] == arr[2]:
		ispos = ispos or True
	elif arr[0] * arr[1] == arr[2]:
		ispos = ispos or True
	elif arr[0] / arr[1] == float(arr[2]):
		ispos = ispos or True
	elif arr[1] / arr[0] == float(arr[2]):
		ispos = ispos or True
	return("Possible" if ispos else "Impossible")
uh = int(input())
out = []
for i in range(uh):
	out += [calc(input().split())]
for thing in out:
	print(thing)
