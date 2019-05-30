def find_sum(s: list, x: int) -> (bool, (int, int)):
    s = sorted(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] + s[j] == x:
            return True, (s[i], s[j])
        elif s[i] + s[j] > x:
            j -= 1
        else:
            i += 1
    return False, None


if __name__ == '__main__':
    s_test = [
        [9, 7, 3, 8, 3, 4, 12, 123, 5, 12],
        [2, 4, 5, 1],
        []
    ]
    x_test = 8
    for i in s_test:
        print(find_sum(i, x_test))
