#https://open.kattis.com/problems/nastyhacks
n = int(input())
nums = [None] * n
for i in range(n):
    nums[i] = input().split(" ")
for i in range(n):
    diff = int(nums[i][1]) - int(nums[i][0])
    ad = int(nums[i][2])
    if diff > ad:
        print("advertise")
    elif diff < ad:
        print("do not advertise")
    else:
        print("does not matter")
