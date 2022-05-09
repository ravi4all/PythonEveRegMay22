#Nested Loops - Loop inside a Loop
#i = 0, j = 0,1,2,3,4
#i = 1, j = 0,1,2,3,4
#i = 2, j = 0,1,2,3,4
#i = 3, j = 0,1,2,3,4
#i = 4, j = 0,1,2,3,4
'''
for i in range(5):
    print("i = {}, ".format(i), end="")
    for j in range(5):
        print("j = {}, ".format(j), end='')
    print()
'''


'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
'''

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print("=" * 50)

'''
*
***
*****
******
*******
'''
for i in range(10):
    if i % 2 != 0:
        for j in range(i):
            print('*', end='')
        print()



