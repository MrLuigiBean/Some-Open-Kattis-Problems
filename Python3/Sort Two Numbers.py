#https://open.kattis.com/problems/sorttwonumbers
nums = input().split()
for i in range(len(nums)):
	nums[i] = int(nums[i])
print(min(nums), max(nums))
