import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize


def find_longest_sequence(root):
    if not root:
        return 0

    def dfs(node):
        if not node:
            return 0, 0
        
        if not node.left and not node.right:
            return 1, 1
            
        llen, lmx = dfs(node.left)
        rlen, rmx = dfs(node.right)

        llen = llen + 1 if node.left and node.left.val == node.val + 1 else 1
        rlen = rlen + 1 if node.right and node.right.val == node.val + 1 else 1

        length = max(llen, rlen)
        return length, max(lmx, rmx, length)
    
    length, mx = dfs(root)
    return mx


print(3 == find_longest_sequence(deserialize('[1,null,4,5,5,6]')))