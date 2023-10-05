from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.tree import TreeNode, deserialize, traverse_level


def create_binary_search_tree(preorder: List[int]) -> TreeNode:
    if not preorder:
        return []
    
    def dfs(nums, l, r):
        if l > r:
            return None

        node = TreeNode(nums[l])
        idx = r

        for i in range(l + 1, r + 1):
            if nums[l] < nums[i]:
                idx = i - 1
                break
                
        node.left = dfs(nums, l + 1, idx)
        node.right = dfs(nums, idx + 1, r)

        return node
    
    return dfs(preorder, 0, len(preorder) - 1)


print(traverse_level(create_binary_search_tree([4, 2, 1, 3, 6, 5])))