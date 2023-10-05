import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize, traverse_level


def traverse_vertically(root: TreeNode) -> [[int]]:
    nodes = collections.defaultdict(lambda: collections.defaultdict(list))

    def traverse(node, y, x):
        nodes[x][y] += node.val,

        if node.left:
            traverse(node.left, y + 1, x - 1)

        if node.right:
            traverse(node.right, y + 1, x + 1)

    traverse(root, 0, 0)

    all_nodes = sorted(nodes.items(), key=lambda p: p[0])
    res = []

    for x, vert in all_nodes:
        items = []
        vert = sorted(vert.items(), key=lambda p: p[0])
        for y, nodes in vert:
            items += sorted(nodes)

        res += items,

    return res


print(traverse_vertically(deserialize('[8,5,7,4,3,2,6]'))) 