from random import choice
from time import time

from typing import List


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

    # 读取待排序数据，100万数据
    a = []
    with open('test_data.txt', 'r', encoding='utf-8') as f:
        while True:
            i = f.readline()
            if i == '':
                break
            a.append(float(i))

    # 内建排序函数
    start_time = time()
    b = sorted(a)
    print(time() - start_time)

    # 使用我实现的快速排序算法进行排序，计时，并判断排序结果是否正确
    start_time = time()
    quick_sort(a[:1000000])
    print(a == b, time() - start_time)
    # 若数列全部相等，则需要比较n(n-1)/2次，即O(n^2) 最差情况
    # 最好是T(n)=2T(n/2)+n,主定理,为O(nlgn)
