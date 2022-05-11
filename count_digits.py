num = 12345
'''
num = num / 10 => 1234
num = num / 10 => 123
num = num / 10 => 12
num = num / 10 => 1
num = num / 10 => 0
'''

count = 0
while num != 0:
    num = num // 10
    #count = count + 1
    count += 1

print("Count is",count)
