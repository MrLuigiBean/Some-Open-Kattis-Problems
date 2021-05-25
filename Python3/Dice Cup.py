#https://open.kattis.com/problems/dicecup
def calc(arr):
    if int(arr[0]) > int(arr[1]): calc(arr[::-1])   
    for i in range(int(arr[0])+1, int(arr[1])+2):
        print(i)    
calc(input().split(" "))
