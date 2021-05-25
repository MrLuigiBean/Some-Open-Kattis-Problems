#https://open.kattis.com/problems/magictrick
word = input()
flag = False
for i in range(len(word)):
    for k in range(len(word)):
        if word[k] == word[i] and i != k:
            flag = True
print(0 if flag else 1)
