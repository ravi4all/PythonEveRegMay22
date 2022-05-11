minRange = int(input("Enter min number : "))
maxRange = int(input("Enter max number : "))

for num in range(minRange, maxRange):
    for i in range(2, num // 2):
        if num % i == 0:
            #print(f"{num} is not a prime number...")
            break
    else:
        print(f"{num} is a prime number...")
