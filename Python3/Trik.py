#https://open.kattis.com/problems/trik
 moves = input()
pos = 1

for char in moves:
    if char == "A" and not(pos == 3):
        if pos == 1:
            pos += 1 
        else: #elif pos == 2:
            pos -= 1 

    if char == "B" and not(pos == 1):
        if pos == 2:
            pos += 1 
        else: #elif pos == 3:
            pos -= 1

    if char == "C" and not(pos == 2):
        if pos == 1:
            pos += 2 
        else: #elif pos == 3:
            pos -= 2

print(pos) 
