import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


head = [6, 7, 4, 3]
k = 2


def rotate_list(head: ListNode, k: int) -> ListNode:
    if not head:
        return None

    n = 0
    node = head
    last = None

    while node:
        if node:
            last = node
        node = node.next
        n += 1

    k = k % n

    if n == 1 or k == 0 or k == n:
        return head
    
    i = 0
    pre = node = head

    while node and i < n - k:
        pre = node
        node = node.next
        i += 1

    last.next = head
    pre.next = None
    head = node
    return head


res = rotate_list(create_linked_list_from_nums(head), k)
print([4, 3, 6, 7] == list_get_nums(res))