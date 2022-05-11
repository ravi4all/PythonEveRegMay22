num = 137

for i in range(2, num // 2):
    if num % i == 0:
        print(f"{num} is not a prime number...")
        break
else:
    print(f"{num} is a prime number...")
