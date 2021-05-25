#https://open.kattis.com/problems/pet
def add(arr):
    return int(arr[0]) + int(arr[1]) + int(arr[2]) + int(arr[3])
winner = 0
hisc = 0
for i in range(1, 6):
     temp = input().split(" ")
     sc = add(temp)
     if sc > hisc:
         hisc = sc
         winner = i
print(str(winner) + " " + str(hisc))
