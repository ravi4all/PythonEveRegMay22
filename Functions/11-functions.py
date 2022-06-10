def temp_convert(c):
    return 9/5 * c + 32

# f = temp_convert(34.5)
# print(f)

temp = [40.5,41.5,38.7,43.4,40.5]

# fah = []
# for i in range(len(temp)):
#     f = temp_convert(temp[i])
#     fah.append(f)

# print(fah)

fah = list(map(temp_convert, temp))
print(fah)