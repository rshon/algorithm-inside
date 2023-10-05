import collections
from typing import List


def return_change(bills: List[int]) -> bool:
    change = collections.defaultdict(int)
    
    for bill in bills:
        left = bill - 50
        
        if left:
            for unit in [200, 100, 50]:
                while change[unit] and left >= unit:
                    left -= unit
                    change[unit] -= 1
        
        if left:
            return False
        
        change[bill] += 1
    
    return True


print(True == return_change([50, 50, 50, 100, 200]))