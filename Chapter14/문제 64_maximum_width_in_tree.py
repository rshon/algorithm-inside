import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize


def get_max_level_width(root: TreeNode) -> int:
    q = collections.deque([(root, 1)])
    mx_width = 0

    while q:
        nq = collections.deque()
        idx = first = q[0][1]

        while q:
            node, idx = q.popleft()

            if node.left:
                nq += (node.left, idx * 2 - 1),
            if node.right:
                nq += (node.right, idx * 2),

        mx_width = max(mx_width, idx - first + 1)
        q = nq

    return mx_width


res = get_max_level_width(deserialize('[1, 2, 3, null, 4, null, 6, null, 7, 10]'))
print(4 == res)