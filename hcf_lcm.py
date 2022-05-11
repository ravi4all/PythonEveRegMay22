x = 90
y = 56

copy_x = x
copy_y = y

while x % y != 0:
    rem = x % y
    x = y
    y = rem

gcd = y
print("HCF :",gcd)
lcm = (copy_x * copy_y) / gcd
print("LCM :",lcm)
