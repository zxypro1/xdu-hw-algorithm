def zero_one_knapsack_back_tracking(items, c):
    items = [(i, items[i][0], items[i][1]) for i in range(len(items))]
    items.sort(key=lambda a: a[1])

    choices_stack = []
    weight_sum = 0
    value_sum = 0
    choices = []
    max_flag = (0, [])
    while True:
        if c - weight_sum >= items[len(choices_stack)][1]:
            choices_stack.append(True)
            weight_sum += items[len(choices_stack)][1]
            value_sum += items[len(choices_stack)][2]
        else:
            choices.append((value_sum, choices_stack))
            if max_flag[0] < value_sum:
                max_flag = (value_sum, choices_stack)

        if len(choices_stack) == len(items):
            pass


if __name__ == '__main__':
    data = [
        (10, 20),
        (20, 30),
        (30, 65),
        (40, 40),
        (50, 60),
    ]
    print(zero_one_knapsack_back_tracking(data, 100))
