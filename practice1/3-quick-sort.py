from random import choice, random
from time import time


def quick_sort(source: list) -> None:
    _quick_sort(source, 0, len(source) - 1)


def _quick_sort(source: list, p: int, r: int) -> None:
    if p < r:
        q, t = partition(source, p, r)
        _quick_sort(source, p, q - 1)
        _quick_sort(source, t + 1, r)


def partition(source: list, p: int, r: int) -> (int, int):
    key = choice(range(p, r + 1))
    source[key], source[r] = source[r], source[key]

    i = p - 1
    j = r
    elem = p
    while elem < j:
        if source[elem] < source[r]:
            i += 1
            source[i], source[elem] = source[elem], source[i]
        elif source[elem] == source[r]:
            j -= 1
            source[elem], source[j] = source[j], source[elem]

        elem += 1

    for k in range(j, r + 1):
        i += 1
        source[i], source[j] = source[j], source[i]
    return i - r + j, i


if __name__ == '__main__':

    # a = []
    # for i in range(1000000):
    #     a.append(1)
    #
    # with open('test_data.txt', 'w', encoding='utf-8') as f:
    #     f.writelines('\n'.join(map(str, a)))

    a = []
    with open('test_data.txt', 'r', encoding='utf-8') as f:
        while True:
            i = f.readline()
            if i == '':
                break
            a.append(float(i))

    b = sorted(a)

    start_time = time()
    quick_sort(a)
    print(a == b, time() - start_time)
