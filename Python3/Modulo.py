#https://open.kattis.com/problems/modulo
nums = [None] * 10
for i in range(10):
    nums[i] = int(input())
mods = []
for i in range(10):
    r = nums[i]%42
    if r not in mods:
        mods += [r]
print(len(mods))
