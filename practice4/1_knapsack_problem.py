from math import inf


def zero_one_knapsack_back_tracking(items, c):
    # （id, weight, value）
    items = [(i, items[i][0], items[i][1]) for i in range(len(items))]
    items.sort(key=lambda a: a[1])

    # 最后一个元素重量无穷大
    # 将没东西装的情况转化为装不下的情况，方便讨论
    items.append((len(items), inf, 0))

    choices_stack = []
    weight_sum = 0
    value_sum = 0
    choices = []
    max_flag = (0, [])
    while True:
        if c - weight_sum >= items[len(choices_stack)][1]:
            weight_sum += items[len(choices_stack)][1]
            value_sum += items[len(choices_stack)][2]
            choices_stack.append(True)
        else:
            choices.append((value_sum, choices_stack.copy()))

            # 记录当前最优选择
            if choices[-1][0] > max_flag[0]:
                max_flag = choices[-1]

            while len(choices_stack) > 0 and not choices_stack[-1]:
                choices_stack.pop()

            # 栈空，遍历完成
            if len(choices_stack) == 0:
                for i in choices:
                    print(i)
                print()
                res = (max_flag[0], [])
                for i in range(len(max_flag[1])):
                    if max_flag[1][i]:
                        res[1].append(items[i][0])
                return res

            choices_stack[-1] = False
            weight_sum -= items[len(choices_stack)-1][1]
            value_sum -= items[len(choices_stack)-1][2]


if __name__ == '__main__':
    data = [
        (10, 20),
        (20, 30),
        (30, 65),
        (40, 40),
        (50, 60),
    ]
    print(zero_one_knapsack_back_tracking(data, 100))
