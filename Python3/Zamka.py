#https://open.kattis.com/problems/zamka
def calc(i):
    sum = 0
    for n in range(len(str(i))):
        sum += int(str(i)[n])
    return sum
l = int(input())
d = int(input())
x = int(input())
n = d
m = 0
for i in range(l,d+1):
    if calc(i) == x:
        if i > m: m = i
        if i < n: n = i
print(n)
print(m)
