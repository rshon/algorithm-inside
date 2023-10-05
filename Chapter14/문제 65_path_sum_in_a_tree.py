import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize


def get_num_paths(root: TreeNode, target: int) -> int:
    if not root:
        return 0

    def dfs(node, target, inc):
        if not node:
            return 0

        cnt = 0
        inc += node.val

        if target == inc:
            cnt = 1

        cnt += dfs(node.left, target, inc)
        cnt += dfs(node.right, target, inc)

        return cnt
    q = collections.deque([root])
    cnt = 0

    while q:
        node = q.popleft()
        if not node:
            continue

        cnt += dfs(node, target, 0)

        if None != node.left:
            q += node.left,

        if None != node.right:
            q += node.right,

    return cnt


print(get_num_paths(deserialize('[5,4,null,1,null,3,4,null,null,5,10]'), 10))