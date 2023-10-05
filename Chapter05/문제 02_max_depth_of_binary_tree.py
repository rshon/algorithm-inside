import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize


def update_depth(node: TreeNode, depth, max_depth):
    if not node:
        return

    if not node.left and not node.right:
       max_depth[0] = max(max_depth[0], depth)
       return

    update_depth(node.left, depth + 1, max_depth)
    update_depth(node.right, depth + 1, max_depth)


root = deserialize('[2,4,1,92,11,null,null,null,null,null,45]')
max_depth = [0]
update_depth(root, 1, max_depth)
print(max_depth[0])
