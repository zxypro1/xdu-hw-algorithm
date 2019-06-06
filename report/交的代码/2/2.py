def lcs(x, y):
    m = len(x)
    n = len(y)

    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i+1][j+1] = c[i][j] + 1
                b[i][j] = 0
            elif c[i][j+1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 1
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = -1

    z = []
    i = m - 1
    j = n - 1
    while i >= 0 and j >= 0:
        if c[i+1][j+1] == c[i][j+1]:
            i -= 1
        elif c[i+1][j+1] == c[i+1][j]:
            j -= 1
        else:
            z.insert(0, x[i])
            i -= 1
            j -= 1

    return ''.join(z)


if __name__ == '__main__':
    datas = [
        ['xzyzzyx', 'zxyyzxz'],
        [
            'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD',
            'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'
        ]
    ]
    for data in datas:
        print(lcs(data[0], data[1]))
