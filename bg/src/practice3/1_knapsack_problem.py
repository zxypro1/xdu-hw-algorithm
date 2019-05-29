def zero_one_knapsack(items, c, step=1):
    n = len(items)
    m = c // step + 1
    result = [[(0, []) for _ in range(m)] for _ in range(n+1)]

    for j in range(m):
        for i in range(n):
            if items[i][0] > j * step:
                result[i][j] = result[i-1][j]
            else:
                sub_q = result[i-1][(j*step-items[i][0])//step]
                result[i][j] = max(result[i-1][j], (items[i][1] + sub_q[0], sub_q[1] + [i, ]))

    return result[n-1][m-1]


def fractional_knapsack(items, c):
    items = [(i, items[i][1] / items[i][0], items[i][0], items[i][1]) for i in range(len(items))]
    items.sort(key=lambda a: a[1], reverse=True)
    weight_sum = 0
    value_sum = 0
    choices = []
    for i in items:
        if i[2] < c - weight_sum:
            value_sum += i[3]
            choices.append((i[0], i[2]))
            weight_sum += i[2]
        else:
            value_sum += i[1] * (c - weight_sum)
            choices.append((i[0], c - weight_sum))
            break
    return value_sum, choices


if __name__ == '__main__':
    data = [
        (10, 20),
        (20, 30),
        (30, 65),
        (40, 40),
        (50, 60),
    ]
    print(zero_one_knapsack(data, 100, 10))
    print(fractional_knapsack(data, 100))
