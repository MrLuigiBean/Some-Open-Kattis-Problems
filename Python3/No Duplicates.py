#https://open.kattis.com/problems/nodup
text = input().split(" ")
norep = True
for i in range(len(text)):
    for k in range(len(text)):
        if not norep:
            break
        if text[i] == text[k] and not(i == k):
            norep = False
print("yes" if norep else "no")
