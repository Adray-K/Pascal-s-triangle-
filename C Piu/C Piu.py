x = int(input())
p = []
for i in range(0, x):
    row = []
    p.append(row)
    for j in range(0, i + 1):
        row.append(1)
        if j == 0 or j == i:
            p[i][j] = 1
        elif i > 1:
            p[i][j] = p[i-1][j-1] + p[i-1][j]

x = len(p)+(len(p)-1)
for a, b in enumerate(p):
    print(' ' * int(x//2), end='')
    for c, d in enumerate(b):
        print(d, end=' ')
    print(' ' * int(x//2))
    x -= 2

