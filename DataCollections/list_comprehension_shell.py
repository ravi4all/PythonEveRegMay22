Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
even = []
for i in range(1,51):
    if i % 2 == 0:
        even.append(i)

        
even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
even = [i for i in range(10)]
even
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [i for i in range(0,51,2)]
even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
even = [i for i in range(0,51) if i % 2 == 0]
even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
even = [i for i in range(5) for j in range(5) if i == j]
even
[0, 1, 2, 3, 4]
even = [[i,j] for i in range(5) for j in range(5) if i == j]
even
[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
