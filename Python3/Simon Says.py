#https://open.kattis.com/problems/simonsays
num = int(input())
simon = [None] * num
for i in range(num):
    simon[i] = input()

for words in simon:
    if "Simon says " in words:
        print(words[len("Simon says "):])
