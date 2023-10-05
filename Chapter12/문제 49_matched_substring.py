
s = 'python'
length = 2
power = 5
modulo = 11
rolling_hash = 5


def find_rolling_hash(s, length, power, modulo, rolling_hash) -> str:
    def get_val(ch):
        return (ord(ch) - ord('a') + 1)

    rh = 0
    weight = 1

    for i in range(length):
        rh += get_val(s[i]) * weight
        weight *= power

    if rh % modulo == rolling_hash:
        return s[:length]

    for i in range(length, len(s)):
        rh += get_val(s[i]) * weight
        rh -= get_val(s[i - length])
        rh = rh // power

        if rh % modulo == rolling_hash:
            return s[i - length + 1: i + 1]
        
    return ""


print('th' == find_rolling_hash(s, length, power, modulo, rolling_hash))