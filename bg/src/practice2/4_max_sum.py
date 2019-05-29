def max_sum(d):
    res = d[0]
    max_i = 0
    max_j = 1
    i = 0
    j = 0
    max_count = 0

    for item in d:
        max_count += item
        j += 1
        if max_count > res:
            res = max_count
            max_i, max_j = i, j
        if max_count <= 0:
            max_count = 0
            i = j
    return res, max_i, max_j


if __name__ == '__main__':
    print(max_sum([-2, 11, -4, 13, -5, -2]))
