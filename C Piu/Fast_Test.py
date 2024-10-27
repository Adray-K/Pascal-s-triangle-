p = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

x = len(p)+(len(p)-1)
for a, b in enumerate(p):
    print(' ' * int(x//2), end='')
    for c, d in enumerate(b):
        print(d, end=' ')
    print(' ' * int(x//2))
    x -= 2

