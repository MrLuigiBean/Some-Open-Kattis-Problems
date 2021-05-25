#https://open.kattis.com/problems/zanzibar
def calc(arr):
    total = 0
    for i in range(len(arr) - 1):   
        if int(arr[i]) * 2 < int(arr[i+1]):
            total += int(arr[i+1]) - 2*int(arr[i])
        else:
            total += 0
    return total
n = int(input())
nums = []
for i in range(n):
    nums += [input().split(" ")]
for thing in nums:
    print(calc(thing))
