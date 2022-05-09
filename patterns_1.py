'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(i):
        print(i, end='')
    print()

print("=" * 30)

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()

print("=" * 30)

'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k, end='')
    print()

print("=" * 30)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    for j in range(5 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

print("=" * 30)


'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
k = 0
for i in range(4):
    for n in range(4 - i):
        print(' ', end='')
    for j in range(i+1):
        k += 1
        print(k, end=' ')
    print()
