#https://open.kattis.com/problems/pieceofcake2
nums = input().split(" ")
h = int(nums[1]) if int(nums[1]) > int(nums[0])/2 else int(nums[0]) - int(nums[1])
v = int(nums[2]) if int(nums[2]) > int(nums[0])/2 else int(nums[0]) - int(nums[2])
print(h*v*4)
