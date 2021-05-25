#https://open.kattis.com/problems/qaly
num = int(input())
total = 0

def mul(array):
    return float(array[0]) * float(array[1])

for i in range(num):
    total += mul(input().split(" "))
print(total
