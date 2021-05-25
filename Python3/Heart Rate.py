#https://open.kattis.com/problems/heartrate
def here(arr):
    b = float(arr[0])
    p = float(arr[1])
    print("{0} {1} {2}".format(60*(b-1)/p, 60*b/p, 60*(b+1)/p))

n = int(input())
mylist =[]
for i in range(n):
    mylist += [input().split(" ")]
for thing in mylist:
    here(thing)
