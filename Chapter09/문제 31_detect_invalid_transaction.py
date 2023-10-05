
transactions = ["Jay,10,900,Seoul", "Rick,30,700,Tokyo", "Jay,40,500,Beijing", "Rick,55,1100,Tokyo"]


def detect_invalid_transaction():
    trs = [tr.split(',') for tr in transactions]
    trs.sort(key=lambda p: (p[0], int(p[1])))
    res = []
    suspicious = set()

    for l, tr in enumerate(trs):
        fraud = False
        r = l + 1

        while r < len(trs) and tr[0] == trs[r][0] and int(tr[1]) + 60 >= int(trs[r][1]):
            if tr[3] != trs[r][3]:
                fraud = True
            r += 1

        if fraud:
            i = l
            while i < r:
                suspicious.add(i)
                i += 1

        if int(tr[2]) > 1000 and l not in suspicious:
            suspicious.add(l)

    for i in sorted(suspicious):
        res += ','.join(trs[i]),

    return res


print(['Jay,10,900,Seoul', 'Jay,40,500,Beijing', 'Rick,55,1100,Tokyo']
       == detect_invalid_transaction())