#https://open.kattis.com/problems/quickestimate
n = int(input())
nums = []
for i in range(n):
	nums += [input()]
for thing in nums:
	print(len(thing))
