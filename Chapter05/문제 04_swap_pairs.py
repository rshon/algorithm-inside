import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    head.val, head.next.val = head.next.val, head.val

    swap_pairs(head.next.next)
    return head


print(list_get_nums(swap_pairs(create_linked_list_from_nums([1,2,3,4]))))