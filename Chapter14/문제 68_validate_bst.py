import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize, traverse_level


def is_bst(root: TreeNode) -> bool:
    if not root:
        return True
    
    def check(node, l, r):
        if not node:
            return True
    
        if not (l < node.val < r):
            return False
        
        return check(node.left, l, min(node.val, r)) and \
            check(node.right, max(node.val, l), r)
    
    return check(root, float('-inf'), float('inf'))


print(is_bst(deserialize('[7,3,5,null,null,4,8]')))