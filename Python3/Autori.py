#https://open.kattis.com/problems/autori
names = input().split("-")
output = ""
for thing in names:
    output += thing[0]
print(output)
