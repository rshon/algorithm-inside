import collections
from typing import List


data = [221, 154, 19]


def validate_utf8_data(data: List[int]) -> bool:
    data = collections.deque(data)
    while data:
        header = data.popleft()
        header = '{:08b}'.format(header)
        ones = 0

        for i in range(5):
            if '1' != header[i]:
                break
            ones += 1

        if not ones:
            continue

        if not (2 <= ones <= 4):
            return False

        ones -= 1

        while data and ones:
            chunk = data.popleft()
            chunk = '{:08b}'.format(chunk)
            if not chunk.startswith('10'):
                return False
            ones -= 1

        if ones > 0:
            return False

    return True


print(validate_utf8_data(data))