from math import inf


def floyd_warshall(w):
    n = len(w)
    d = w.copy()
    pi = [[i if (d[i][j] != inf and i != j) else None for j in range(n)] for i in range(n)]
    for k in range(n):
        pi = [[pi[i][j] if d[i][j] <= d[i][k] + d[k][j] else pi[k][j] for j in range(n)] for i in range(n)]
        d = [[d[i][j] if d[i][j] < d[i][k] + d[k][j] else d[i][k] + d[k][j] for j in range(n)]for i in range(n)]
    return d, pi


def print_result(d_pi):
    d, pi = d_pi
    for i, j in zip(d, pi):
        print(list(zip(i, j)))
    print()


if __name__ == '__main__':
    data = [
        [0,    -1,   3, inf, inf],
        [inf,   0,   3,   2,   2],
        [inf, inf,   0, inf, inf],
        [inf,   1,   5,   0, inf],
        [inf, inf, inf,  -3,   0]
    ]
    print_result(floyd_warshall(data))
