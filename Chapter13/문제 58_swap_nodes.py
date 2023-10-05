import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


nodes = [2, 1, 4, 3]


def swap_every_two_nodes(node: ListNode) -> ListNode:
    if not node or not node.next:
        return node
    
    last = node.next
    node.next = swap_every_two_nodes(node.next.next)
    last.next = node
    
    return last


res = swap_every_two_nodes(create_linked_list_from_nums(nodes))
print([1, 2, 3, 4] == list_get_nums(res))
