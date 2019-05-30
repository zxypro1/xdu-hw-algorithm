def n_queen(n: int) -> list:
    def can_set_queen(qs, location):
        for j in range(len(qs)):
            if qs[j] == location:
                return False
            if qs[j] + len(qs) - j == location:
                return False
            if qs[j] - len(qs) + j == location:
                return False
        return True

    queens_stack = []
    res = []
    queens_stack.append(0)
    last = 0
    while True:
        for i in range(last, n):
            if can_set_queen(queens_stack, i):
                queens_stack.append(i)
                last = 0
                break
        else:
            if len(queens_stack):
                last = queens_stack.pop() + 1
            else:
                return res
        if len(queens_stack) == n:
            res.append(tuple(queens_stack))
            last = queens_stack.pop() + 1


if __name__ == '__main__':
    for result in n_queen(8):
        print(result)
    print(len(n_queen(8)))
