#https://open.kattis.com/problems/sevenwonders
cards = input()
t = 0
c = 0
g = 0
total = 0
for char in cards:
    if char == 'T': t += 1
    elif char == 'C':   c += 1
    else: g += 1
sort = [t, c, g]
sort.sort()
total = t**2 + c**2 + g**2 + 7 * sort[0]
print(total)
