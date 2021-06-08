#https://open.kattis.com/problems/railroad2
x, y = input().split()
print("possible" if (2*int(x)+int(y))%2==0 else "impossible")
