#https://open.kattis.com/problems/cold
n = int(input())
temp = input().split(" ")
counter = 0
for thing in temp:
    if int(thing) < 0:
        counter += 1
print(counter)
