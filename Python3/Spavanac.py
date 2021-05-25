#https://open.kattis.com/problems/spavanac
alarm = input().split(" ")
alarm[1] = int(alarm[1]) - 45
if alarm[1] < 0:
    alarm[1] += 60
    alarm[0] = int(alarm[0]) -1
    if alarm[0] < 0:
        alarm[0] = 23
print("{0} {1}".format(alarm[0], alarm[1]))
