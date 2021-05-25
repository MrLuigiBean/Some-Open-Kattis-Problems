#https://open.kattis.com/problems/shatteredcake
#3.73s/6s CPU Time Limit! AWESOME!!!
width = int(input())
num = int(input())
area = 0

def mul(array):
	return int(array[0]) * int(array[1])

for i in range(num):
	area += mul(input().split(" "))
print(area//width)

"""
5.85/6 CPU Time limit...

width = int(input())
num = int(input())
area = 0
temp = [None] * num
for i in range(num):
	temp[i] = input().split(" ")
	area += int(temp[i][0]) * int(temp[i][1])
print(area//width)
"""
