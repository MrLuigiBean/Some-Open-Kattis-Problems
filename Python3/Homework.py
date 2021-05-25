#https://open.kattis.com/problems/heimavinna
qsn = input().split(";")
total = 0
for i in range(len(qsn)):
    qsn[i] = qsn[i].split("-")
for i in range(len(qsn)):
    total += 1 if len(qsn[i]) == 1 else int(qsn[i][1]) - int(qsn[i][0]) +1
print(total)
