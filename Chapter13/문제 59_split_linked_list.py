import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


head = [1,2,3,4,5,6,7,8]
k = 3


def split_linked_list(head, k):
    if not head:
        return [None for _ in range(k)]

    nodes = []
    while head:
        nodes += head,
        head = head.next

    n = len(nodes)
    part = n // k
    remainder = n % k

    i = 0
    chunks = []

    while i < n:
        until = i + part
        chunks += nodes[i],

        while i < until and i < n:
            i += 1

        if i < n and remainder:
            remainder -= 1
            i += 1

        nodes[i - 1].next = None

    while chunks and len(chunks) < k:
        chunks += None,

    return chunks


split_linked_list(create_linked_list_from_nums(head), k)
