#https://open.kattis.com/problems/bela
def dom(x):
    values = {"A":11, "K":4, "Q":3, "J":20, "T":10, "9":14}
    return(values[x] if x in values else 0)
def rec(x):
    values = {"A":11, "K":4, "Q":3, "J":2, "T":10}
    return(values[x] if x in values else 0)
info = input().split(" ")
cards = []
score = 0
for i in range(4*int(info[0])):
    cards += [input()]
for card in cards:
    if card[1] ==  info[1]: #dom
        score += dom(card[0])
    else: #rec
        score += rec(card[0])
print(score)
