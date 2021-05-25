#https://open.kattis.com/problems/chanukah
def fadd(x):
    return(int(x)//2 *(int(x)+1) if int(x)%2==0 else int(x)//2 *(int(x)+1) + int(x)//2 +1 )
n = int(input())
nums = []
for i in range(n):
    nums += [input().split(" ")]
for thing in nums:
    print("{0} {1}".format(thing[0], fadd(thing[1]) + int(thing[1])))
