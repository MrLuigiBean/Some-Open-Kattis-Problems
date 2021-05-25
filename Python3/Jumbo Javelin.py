#https://open.kattis.com/problems/jumbojavelin
n = int(input())
final = 0
for i in range(n):
    final += int(input())
print(final-n+1)
