#https://open.kattis.com/problems/ofugsnuid
n = int(input())
nums = []
for i in range(n):
    nums += [input()]
for i in range(n):
    print(nums[-i-1])
