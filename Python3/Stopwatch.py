#https://open.kattis.com/problems/stopwatch
size = int(input())
times = [None] * size
for i in range(size):
    times[i] = int(input())

if size % 2 == 1:
    print("still running")
else: # even sizes
    output = 0
    for i in range(size//2): # 0, 1
        output += times[2*i+1] - times[2*i]
    print(output)
