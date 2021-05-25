#https://open.kattis.com/problems/sibice
import math
num = input().split(" ")
max = math.sqrt(int(num[1]) ** 2 + int(num[2]) ** 2)
matches = [None] * int(num[0])
for i in range(int(num[0])):
    matches[i] = int(input())   
for i in range(int(num[0])):
    print("DA" if matches[i] <= max else "NE")
