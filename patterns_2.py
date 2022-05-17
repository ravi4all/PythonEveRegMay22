'''
1
131
13531
1357531
135797531
'''
for i in range(1,6):
    for j in range(1, 2*i-1, 2):
        print(j, end='')
    for k in range(2*i-1, 0, -2):
        print(k, end='')
    print()
