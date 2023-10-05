
temperature = [65, 68, 67, 75, 70, 69, 72, 74]


def get_num_days_to_wait(temperatures: [int]) -> [int]:
    if not temperatures:
        return []

    n = len(temperatures)
    res = [0]*n
    stk = [(temperatures[0], 0)]

    for i in range(1, len(temperatures)):
        while stk and stk[-1][0] < temperatures[i]:
            val, idx = stk.pop()
            res[idx] = i - idx

        stk += (temperatures[i], i),

    return res


print([1, 2, 1, 0, 2, 1, 1, 0] == get_num_days_to_wait(temperature))