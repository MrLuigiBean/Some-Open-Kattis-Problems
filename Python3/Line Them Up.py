#https://open.kattis.com/problems/lineup
num = int(input())
while num < 2 or num > 20:
  num = int(input("Hey! Number between 2 and 20! "))

names = [None] * num
for i in range(num):
  name = input()
  while len(name) < 2 or len(name) > 12:
    name = input("Hey! Names between 2 and 12 characters! ") 
  names[i] = name 

inc = 0
dec = 0
for i in range(num-1):
    temp = names[i] < names[i+1]
    if temp == True:
        inc+=1
    else:
        dec+=1

if dec == 0:
  print("INCREASING")
elif inc == 0:
  print("DECREASING")
else:
  print("NEITHER")
