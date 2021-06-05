#https://open.kattis.com/problems/reversebinary
n = int(input())
b = bin(n)
rev = b[:1:-1]
sum = 0
for i in range(len(rev)):
	sum += int(rev[len(rev)-i-1]) * 2**(i)
print(sum)
