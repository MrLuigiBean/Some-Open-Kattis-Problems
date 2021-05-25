#https://open.kattis.com/problems/filip
def comp(arr):
    print(int(arr[0][::-1]) if int(arr[0][::-1]) > int(arr[1][::-1]) else int(arr[1][::-1]))
comp(input().split(" "))
