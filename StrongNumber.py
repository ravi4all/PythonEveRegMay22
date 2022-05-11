num = 145
sum = 0
temp = num

while(temp > 0):
    fact = 1
    rem = temp % 10
    for i in range(rem, 0, -1):
        fact = fact * i
    sum += fact
    temp = temp // 10

if sum == num:
    print("Strong number...")
else:
    print("Not strong number...")
