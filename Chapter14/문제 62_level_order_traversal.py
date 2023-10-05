import collections
from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize


def do_level_order_from_bottom(root: List[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = collections.deque([root])
    lines = []
    
    while q:
        nq = collections.deque()
        line = []
        
        while q:
            node = q.popleft()
            line += node.val,
            
            if node.left:
                nq += node.left,
            
            if node.right:
                nq += node.right,
        
        q = nq
        lines.insert(0, line)
    
    return lines


res = do_level_order_from_bottom(deserialize('[5, 11, 15, 1, 2, null, 6]'))
print([[1, 2, 6], [11, 15], [5]] == res)