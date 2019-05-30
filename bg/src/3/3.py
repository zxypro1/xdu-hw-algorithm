from math import inf


def bellman_ford(w, s):
    n = len(w)

    # init
    g = [(inf, None) for _ in range(n)]
    g[s] = (0, None)

    edges = []
    for i in range(n):
        for j in range(n):
            if w[i][j] != inf:
                edges.append((i, j))
    for k in range(n-1):
        for edge in edges:
            if g[edge[1]][0] > g[edge[0]][0] + w[edge[0]][edge[1]]:
                g[edge[1]] = (g[edge[0]][0] + w[edge[0]][edge[1]], edge[0])
    for edge in edges:
        if g[edge[1]][0] > g[edge[0]][0] + w[edge[0]][edge[1]]:
            return False, g
    return True, g


def print_result(res):
    if res[0]:
        for i in res[1]:
            print(i)
    else:
        print('False')


if __name__ == '__main__':
    data = [
        [inf,  -1,   3, inf, inf],
        [inf, inf,   3,   2,   2],
        [inf, inf, inf, inf, inf],
        [inf,   1,   5, inf, inf],
        [inf, inf, inf,  -3, inf]
    ]
    print_result(bellman_ford(data, 0))
