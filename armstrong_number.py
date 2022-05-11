num = 153
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == num:
    print(f"{num} is armstrong number...")
else:
    print(f"{num} is not armstrong number...")
