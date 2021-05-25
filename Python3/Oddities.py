#https://open.kattis.com/problems/oddities
n = int(input())
mylist = [None] * n
for i in range(n):
    mylist[i] = int(input())
for i in range(n):
    print(str(mylist[i]) +" is odd" if mylist[i]%2==1 else str(mylist[i]) +" is even")
