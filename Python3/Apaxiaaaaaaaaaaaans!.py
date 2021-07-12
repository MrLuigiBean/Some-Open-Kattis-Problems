#https://open.kattis.com/problems/apaxiaaans
name = input()
newname = ""
for i in range(len(name)-1):
	if name[i] != name[i+1]:
		newname += name[i]
print(newname + name[-1])
