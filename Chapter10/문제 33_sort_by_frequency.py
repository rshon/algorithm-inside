import collections


s = "happoap"


def sort_by_frequency(s: str) -> str:
    freq = sorted(collections.Counter(s).items(), key=lambda p: p[1], reverse=True)
    return ''.join([k*v for k, v in freq])


print("pppaaho" == sort_by_frequency(s))