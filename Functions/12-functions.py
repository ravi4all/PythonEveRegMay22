def even(num):
    return num % 2 == 0

# print(even(6))
numbers = [2,1,3,4,56,213,54,23,6,4,41]

evenNum = list(filter(even, numbers))
print(evenNum)