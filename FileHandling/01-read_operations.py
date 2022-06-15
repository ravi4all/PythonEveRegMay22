file = open('file_1.txt', 'r')   # by default file will open in read mode
# data = file.read()
# print(data)

# line = file.readline()
# print(line)

# lines = file.readlines()
# print(lines)

file.seek(20)
data = file.read(10)
print(data)

file.close()
