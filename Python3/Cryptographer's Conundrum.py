#https://open.kattis.com/problems/conundrum
ciphertext = input()
size = len(ciphertext)
pertext = (size//3)*"PER"
counter = 0
for i in range(size):
	if ciphertext[i] != pertext[i]:
		counter += 1
print(counter)
