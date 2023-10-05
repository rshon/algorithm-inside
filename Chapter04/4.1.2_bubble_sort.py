
a = [2, 1, 0, 4]
n = len(a)

for i in range(n - 1):
    for j in range(1, n - i):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
