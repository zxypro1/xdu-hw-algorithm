from math import inf


def shortest_path_in_multistage_graph(mg):
    n = len(mg)
    res = [(None, inf) for _ in range(n)]
    res[0] = ([0, ], 0)
    active_node = [0, ]

    while active_node:
        new_active_node = []
        for node in active_node:
            for j in range(n):
                if res[node][1] + mg[node][j] < res[j][1]:
                    res[j] = (res[node][0] + [j, ], res[node][1] + mg[node][j])
                    if new_active_node.count(j) == 0:
                        new_active_node.append(j)
        active_node = new_active_node

    return res[n-1]


if __name__ == '__main__':

    data = [
        #  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
        [0  , 5  , 3  , inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],  # 0
        [inf, 0  , inf, 1  , 3  , 6  , inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],  # 1
        [inf, inf, 0  , inf, 8  , 7  , 6  , inf, inf, inf, inf, inf, inf, inf, inf, inf],  # 2
        [inf, inf, inf, 0  , inf, inf, inf, 6  , 8  , inf, inf, inf, inf, inf, inf, inf],  # 3
        [inf, inf, inf, inf, 0  , inf, inf, 3  , 5  , inf, inf, inf, inf, inf, inf, inf],  # 4
        [inf, inf, inf, inf, inf, 0  , inf, inf, 3  , 3  , inf, inf, inf, inf, inf, inf],  # 5
        [inf, inf, inf, inf, inf, inf, 0  , inf, 8  , 4  , inf, inf, inf, inf, inf, inf],  # 6
        [inf, inf, inf, inf, inf, inf, inf, 0  , inf, inf, 2  , 2  , inf, inf, inf, inf],  # 7
        [inf, inf, inf, inf, inf, inf, inf, inf, 0  , inf, inf, 1  , 2  , inf, inf, inf],  # 8
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , inf, 3  , 3  , inf, inf, inf],  # 9
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , inf, inf, 3  , 5  , inf],  # 10
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , inf, 5  , 2  , inf],  # 11
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , 6  , 6  , inf],  # 12
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , inf, 4  ],  # 13
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  , 3  ],  # 14
        [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0  ],  # 15
    ]
    print(shortest_path_in_multistage_graph(data))
