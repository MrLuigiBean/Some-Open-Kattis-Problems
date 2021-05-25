#https://open.kattis.com/problems/batterup
n = int(input())
sum = 0
count = 0
nums = input().split(" ")
for thing in nums:
    if int(thing) == -1:
        count += 1
        sum += 0
    else:
        sum += int(thing)
print(sum/(n-count))
