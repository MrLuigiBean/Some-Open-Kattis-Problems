#https://open.kattis.com/problems/transitwoes
times = input().split(" ")
walk = input().split(" ")
ride = input().split(" ")
wait = input().split(" ")
grand = []
for i in range(int(times[2])):
    grand += [walk[i]]
    grand += [wait[i]]
    grand += [ride[i]]
grand += walk[-1]
total = 0
for i in range(len(grand)):
    if (i-1)%3 == 0: 
        total += int(grand[i]) - total%int(grand[i]) if total%int(grand[i]) != 0 else 0
    else:
        total += int(grand[i])
print("yes" if total < (int(times[1]) - int(times[0])) else "no")
