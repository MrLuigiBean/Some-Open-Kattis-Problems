#https://open.kattis.com/problems/bijele
nums = input().split(" ")
out = [None] * 6
for i in range(6):
    out[i] = str(std[i] - int(nums[i]))
print(" ".join(out))
