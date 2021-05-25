#https://open.kattis.com/problems/pot
num = int(input())
output = 0
def pow (n):
    return (n//10) ** (n%10)
for i in range(num):
    output += pow(int(input()))
print(output)
