#https://open.kattis.com/problems/grassseed
def mul(arr):
    return float(arr[0]) * float(arr[1])
c = float(input()) 
n = int(input()) 
area = 0
for i in range(n):
    area += mul(input().split(" "))
print(c * area)
