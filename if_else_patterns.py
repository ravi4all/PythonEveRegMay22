'''
1010101
1010101
1010101
1010101
1010101
'''
for i in range(5):
    for j in range(5):
        if j % 2 != 0:
            print('0', end='')
        else:
            print('1', end='')
    print()

print("=" * 20)

'''
11111
00000
11111
00000
11111
'''
for i in range(5):
    for j in range(5):
        if i % 2 != 0:
            print('0', end='')
        else:
            print('1', end='')
    print()

print("=" * 20)

'''
10101
01010
10101
01010
10101
'''
k = 0
for i in range(5):
    for j in range(5):
        if k % 2 == 0:
            print('1', end='')
        else:
            print('0', end='')
        k += 1
    print()

print("=" * 20)

'''
11111
10001
10001
10001
11111
'''
rows = 5
cols = 5
for i in range(1, rows+1):
    for j in range(1, cols+1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print('1', end='')
        else:
            print('0', end='')
    print()


print("=" * 20)

'''
11111
11111
11011
11111
11111
'''
rows = 7
cols = 7
for i in range(rows):
    for j in range(cols):
        if rows // 2 == i and cols // 2 == j:
            print('0', end='')
        else:
            print('1', end='')
    print()


print("=" * 20)

'''
11011
11011
00000
11011
11011
'''
rows = 7
cols = 7
for i in range(rows):
    for j in range(cols):
        if rows // 2 == i or cols // 2 == j:
            print('0', end='')
        else:
            print('1', end='')
    print()

print("=" * 20)







