#https://open.kattis.com/problems/harshadnumbers
n = input()
found = False
while not found:
    temp = 0
    for i in range(len(n)):
        temp += int(n[i])
    if int(n) % temp == 0:
        print(n)
        found = True
    n = str(int(n) + 1)
