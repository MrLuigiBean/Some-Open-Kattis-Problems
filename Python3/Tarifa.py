#https://open.kattis.com/problems/tarifa
limit = int(input())
size = int(input())
use = [None] * size
for i in range(size):
    use[i] = int(input())
final = (size + 1) * limit
for i in range(size):
    final -= use[i]
print(final)
