data = [l for l in open('input.txt')]

def is_xmas(s, x, y, a, b):
    for i in ['M', 'A', 'S']:
        x += a
        y += b
        if x < 0 or x >= len(s) or y < 0 or y >= len(s[0]) or s[x][y] != i:
            return False
    return True

def count_xmas(s):
    c = 0
    for i in range(len(s)):
        for j in range(len(s[0])-1):
            if s[i][j] == 'X':
                c += is_xmas(s, i, j, -1, -1) + is_xmas(s, i, j, 1, 1) + is_xmas(s, i, j, -1, 1) + is_xmas(s, i, j, 1, -1) + is_xmas(s, i, j, 0, -1) + is_xmas(s, i, j, 0, 1) + is_xmas(s, i, j, -1, 0) + is_xmas(s, i, j, 1, 0)
    return c

def is_x_mas(s, x, y):
    a, b = s[x-1][y-1], s[x-1][y+1]
    c, d = s[x+1][y-1], s[x+1][y+1]

    x1 = (a == 'M' or a == 'S') and (a==c or a==b)
    x2 = (d != a) and (d == 'M' or d == 'S') and (d == b or d == c)

    return x1 and x2


def count_x_mas(s):
    c = 0
    for i in range(1, len(s)-1):
        for j in range(1,len(s[0])-2):
            if s[i][j] == 'A':
                c += is_x_mas(s, i, j)
    return c

print(count_xmas(data))
print(count_x_mas(data))