#https://open.kattis.com/problems/cetvrta
def calc(arr):  
    return(arr[0] if arr[0] - arr[1] != 0 else arr[2])
nums = []
for i in range(3):
    nums += [input().split(" ")]
x = []
y = []
for i in range(3):
    x += [int(nums[i][0])]
    y += [int(nums[i][1])]
x.sort()
y.sort()
print("{0} {1}".format(calc(x), calc(y)))
