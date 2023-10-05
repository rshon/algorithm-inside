

power = 2
modulo = power ** 63 - 1


def calc_rolling_hash(s, n):
    rh = 0
    for i in range(n):
        rh *= power
        rh += ord(s[i])
        rh %= modulo

    return rh


def find_substr_rabin_karp(src, part, rh, target):
    weight = pow(power, len(part), modulo)
    
    for i in range(len(part), len(src)):
        rh *= power
        rh -= ord(src[i - len(part)]) * weight
        rh += ord(src[i])
        rh %= modulo

        if target == rh:
            return i - len(part) + 1
            
    return -1


def find_substr(src, part):
    target = calc_rolling_hash(part, len(part))
    rh = calc_rolling_hash(src, len(part))
    if target == rh:
        return 0

    return find_substr_rabin_karp(src, part, rh, target)


idx = find_substr('ababac', 'abac')
if -1 != idx:
    print('found @', idx)