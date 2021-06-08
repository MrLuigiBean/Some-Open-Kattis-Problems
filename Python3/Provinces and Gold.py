#https://open.kattis.com/problems/provincesandgold
g, s, c = input().split()
buypow = 3*int(g) + 2*int(s) + int(c)
out = ""
#victory cards
if buypow >=8:
	out += "Province or "
elif buypow >=5:
	out += "Duchy or "
elif buypow>=2:
	out += "Estate or "
else:
	out
#treasure cards
if buypow >=6:
	out += "Gold"
elif buypow >=3:
	out += "Silver"
else:
	out += "Copper"
print(out)
