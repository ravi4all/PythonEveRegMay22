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

print("=" * 20)

'''
11111
11111
11011
11111
11111
'''

print("=" * 20)

'''
11011
11011
00000
11011
11011
'''

print("=" * 20)
'''
1
131
13531
1357531
135797531
'''








