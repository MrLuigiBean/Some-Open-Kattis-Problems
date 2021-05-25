#https://open.kattis.com/problems/carrots
num = input().split(" ")
eh = [None] * int(num[0])
for i in range(int(num[0])):
    eh[i] = input()
print(int(num[1]))
