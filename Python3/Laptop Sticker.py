#https://open.kattis.com/problems/laptopsticker
nums = input().split(" ")
wc = int(nums[0])
hc = int(nums[1])
ws = int(nums[2])
hs = int(nums[3])
print("1" if wc-ws >= 2 and hc-hs >= 2 else "0")
