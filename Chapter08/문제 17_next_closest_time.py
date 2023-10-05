import bisect


def get_next_time(time):
    time = ''.join([ch for ch in time if ch.isdigit()])

    def convert(time):
        return time[:2] + ':' + time[2:]

    def permutate(seq, seqs):
        if len(seq) == len(time):
            hour = int(seq[:2])
            minute = int(seq[2:])
            if 0 <= hour <= 24 and 0 <= minute < 60 and not (hour == 24 and minute > 0):
                seqs.append(seq)
            return
        
        for i in range(len(time)):
            permutate(seq + time[i], seqs)

    seqs = []
    permutate('', seqs)
    seqs.sort()

    idx = bisect.bisect_right(seqs, time)
    if idx == len(seqs):
        idx = 0

    return convert(seqs[idx])


print(get_next_time ("19:34"))