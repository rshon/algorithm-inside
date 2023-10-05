from typing import List
import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


def swap_pairs_01(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    head.val, head.next.val = head.next.val, head.val
    self.swap_pairs(head.next.next)
    return head


def swap_pairs_02(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    second = head.next
    head.next = self.swap_pairs(head.next.next)
    second.next = head
    return second
