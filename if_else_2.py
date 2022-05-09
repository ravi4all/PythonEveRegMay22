a,b,c = 12,14,16

'''
if a > b and a > c:
    print("A is greatest...")
elif b > c and b > a:
    print("B is greatest...")
else:
    print("C is greatest")
'''

res = "A" if a > b and a > c else "B" if b > c and b > a else "C"
print(res,"is greatest...")
