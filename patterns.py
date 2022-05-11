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
*********
 *******
  *****
   ***
    *
'''
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(' ', end='')
    for k in range(2*i - 1):
        print('*', end='')
    print()

print("=" * 30)

'''
    *
   * *
  *   *
 *     *
*********
'''
for i in range(5):
    for j in range(5 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        if k == 0 or k == 2*i or i == 4:
            print('*', end='')
        else:
            print(" ", end='')
    print()











