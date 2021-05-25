#https://open.kattis.com/problems/lastfactorialdigit
def nf(x):
    if x<=1:
        return 1
    else:
        return (x*nf(x-1))%10
n = int(input())
nums = []
for i in range(n):
    nums += [int(input())]
for i in nums:
    print(nf(i))
