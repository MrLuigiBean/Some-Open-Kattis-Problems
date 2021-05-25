#https://open.kattis.com/problems/fizzbuzz
#0.05 sec
line = input().split(" ")
low = int(line[0])
high = int(line[1])
num = int(line[2])
# the fact that this took as long as it did makes me :(
for i in range(num+1):
    output = ""
    if i == 0:
        continue
    if i % low == 0:
        output += "Fizz"
    if i % high == 0:
        output += "Buzz"
    
    if output == "":
        output = str(i) 

    print(output)
