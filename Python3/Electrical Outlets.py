#https://open.kattis.com/problems/electricaloutlets
def calc(arr):
    sum = 0
    for i in range(int(arr[0])):
        sum += int(arr[i+1])
    return sum - int(arr[0]) + 1
n = int(input())
nums = []
for i in range(n):
    nums += [input().split(" ")]
for thing in nums:
    print(calc(thing))
