# def add(x,y):
#     return x + y

# add = lambda x,y : x + y
# add(3,4)

temp = [40.5,41.5,38.7,43.4,40.5]
fah = list(map(lambda c : 9/5 * c + 32, temp))
print(fah)
