#https://open.kattis.com/problems/alphabetspam
string = input()
ws = 0
lc = 0
uc = 0
sy = 0
for char in string:
    if char == "_":
        ws += 1
    elif char >= 'a' and char <= 'z': 
        lc += 1
    elif char >= 'A' and char <= 'Z':  
        uc += 1
    else:
        sy += 1
print(ws/len(string))
print(lc/len(string))
print(uc/len(string))
print(sy/len(string))
