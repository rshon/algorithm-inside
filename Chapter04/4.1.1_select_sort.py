

a = [2, 1, 0, 4]
n = len(a)


for i in range(n - 1):
    mn_val = a[i]
    mn_idx = i

    for j in range(i + 1, n):
        if mn_val > a[j]:
            mn_val = a[j]
            mn_idx = j
    a[i], a[mn_idx] = a[mn_idx], a[i]
