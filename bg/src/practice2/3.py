def longest_common_substring(s1: str, s2: str) -> str:
    m = len(s1)
    n = len(s2)
    max_flag = (0, 0)  # 以s1中的位置为准
    flag_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                flag_matrix[i+1][j+1] = flag_matrix[i][j] + 1
                if flag_matrix[i+1][j+1] > max_flag[0]:
                    max_flag = (flag_matrix[i+1][j+1], i + 1)

    return s1[max_flag[0]-max_flag[1]: max_flag[0]]


if __name__ == '__main__':
    datas = [
        ['xzyzzyx', 'zxyyzxz'],
        [
            'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD',
            'MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG'
        ]
    ]
    for data in datas:
        print(longest_common_substring(data[0], data[1]))