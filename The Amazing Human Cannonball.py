#https://open.kattis.com/problems/humancannonball2
#LONGEST INDIVIDUAL LINE OF CODE EVER
import math
def calc(arr):
	return "Safe" if float(arr[3])+1 <= float(arr[2])*math.tan(math.radians(float(arr[1]))) - (9.81/2)*(float(arr[2])/ (float(arr[0])*math.cos(math.radians(float(arr[1])))) )**2 <= float(arr[4])-1 else "Not Safe"
n = int(input())
nums = []
for i in range(n):
	nums += [input().split(" ")]
for thing in nums:
	print(calc(thing))
