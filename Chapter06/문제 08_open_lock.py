from typing import List
import collections


def open_lock(deadends: List[str], unLockNum: str) -> int:
    q = collections.deque([('0000', 0)])
    visited = set('0000')
    
    while q:
        curNum, dist = q.popleft()            
        if curNum in deadends:
            continue
        
        if curNum == unLockNum:
            return dist
        
        for i in range(4):
            for inc in [1, -1]:
                diff = str((int(curNum[i]) + inc)%10)
                nextNum = curNum[:i] + diff + curNum[i + 1:]
                if nextNum in visited:
                    continue
                q += (nextNum, dist + 1),
                visited.add(nextNum)
    
    return -1


print(open_lock(["0201","0101","0102","1212","2002"], "0202"))