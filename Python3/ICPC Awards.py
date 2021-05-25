#https://open.kattis.com/problems/icpcawards
n = int(input())
teams = {}
for i in range(n):
    temp = input().split(" ")
    if temp[0] not in teams:
        teams[temp[0]] = temp[1]

counter = 0
for thing in teams:
    if counter < 12:
        print(thing + " " + teams[thing])
        counter += 1
