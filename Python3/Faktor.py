#https://open.kattis.com/problems/faktor
def comp(arr):
    print(int(arr[0])*int(arr[1]) if int(arr[0])<2 else int(arr[0])*(int(arr[1])-1)+1)
comp(input().split(" "))
