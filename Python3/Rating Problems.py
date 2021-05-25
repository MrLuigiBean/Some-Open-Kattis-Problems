#https://open.kattis.com/problems/ratingproblems

n = input().split(" ")
sum = 0
for i in range(int(n[1])):
    sum += int(input())
print("{0} {1}".format(((int(n[0]) - int(n[1])) * -3.0 + sum)/ int(n[0]),((int(n[0]) - int(n[1])) * 3.0 + sum)/ int(n[0])))
