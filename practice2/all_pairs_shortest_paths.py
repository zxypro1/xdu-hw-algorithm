import math


def extend_shortest_paths(l, w):
    n = len(l)
    l2 = []
    for i in range(n):
        l2.append([])
        for j in range(n):
            l2[i].append(math.inf)
            for k in range(n):
                if l2[i][j] > l[i][k] + w[k][j]:
                    l2[i][j] = l[i][k] + w[k][j]
    return l2


def slow_all_pairs_shortest_paths(w):
    n = len(w)
    l = w.copy()
    print('L1')
    print_result(l)
    for m in range(n - 2):
        l = extend_shortest_paths(l, w)
        print(f'L{m+2}')
        print_result(l)


def faster_all_pairs_shortest_paths(w):
    n = len(w)
    l = w.copy()
    print('L1')
    print_result(l)
    m = 1
    while m < n - 1:
        l = extend_shortest_paths(l, l)
        m = 2 * m
        print(f'L{m}')
        print_result(l)


def floyd_warshall(w):
    n = len(w)
    d = w.copy()
    print('D0')
    print_result(d)
    for k in range(n):
        d2 = []
        for i in range(n):
            d2.append([])
            for j in range(n):
                d2[i].append(d[i][j] if d[i][j] < d[i][k] + d[k][j] else d[i][k] + d[k][j])
        d = d2
        print(f'D{k+1}')
        print_result(d)


def print_result(l):
    for i in l:
        print(i)
    print()


data = [
    [0,        math.inf, math.inf, math.inf,       -1, math.inf],
    [1,               0, math.inf,        2, math.inf, math.inf],
    [math.inf,        2,        0, math.inf, math.inf, -8],
    [-4,       math.inf, math.inf,        0,        3, math.inf],
    [math.inf,        7, math.inf, math.inf,        0, math.inf],
    [math.inf,        5,       10, math.inf, math.inf, 0]
]
data2 = [
    [0, 3, 8, math.inf, -4],
    [math.inf, 0, math.inf, 1, 7],
    [math.inf, 4, 0, math.inf, math.inf],
    [2, math.inf, -5, 0, math.inf],
    [math.inf, math.inf, math.inf, 6, 0]
]
slow_all_pairs_shortest_paths(data)
print('-----')
faster_all_pairs_shortest_paths(data)
print('-----')
floyd_warshall(data)

