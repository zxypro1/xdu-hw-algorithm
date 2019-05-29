import math


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for j in range(n)] for i in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = math.inf
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    m[j][i] = k

    print(m[0][n-1])
    print_optimal_parens(m, 0, n - 1, end='\n')


def print_optimal_parens(m, i, j, end=''):
    if i == j:
        print(f'A{i}', end='')
    else:
        print('(', end='')
        print_optimal_parens(m, i, m[j][i])
        print_optimal_parens(m, m[j][i] + 1, j)
        print(')', end=end)


if __name__ == '__main__':
    matrix_chain_order([3, 5, 2, 1, 10])
    matrix_chain_order([2, 7, 3, 6, 10])
    matrix_chain_order([10, 3, 15, 12, 7, 2])
    matrix_chain_order([7, 2, 4, 15, 20, 5])

