import collections
from typing import List
from typing import Optional
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


head = [3, 4, 0, 2, 1]
nums = [1, 3, 4]


def get_num_of_groups(head: Optional[ListNode], nums: List[int]) -> int:
    pos = collections.defaultdict(int)
    i = 0

    while head != None:
        pos[head.val] = i
        head = head.next
        i += 1

    if 0 == i:
        return 0

    existences = [False]*i

    for num in nums:
        if num in pos:
            existences[pos[num]] = True

    cnt = 0
    pre = existences[0]
    if pre:
        cnt += 1

    for val in existences[1:]:
        if True == val and False == pre:
            cnt += 1
        pre = val

    return cnt


print(2 == get_num_of_groups(create_linked_list_from_nums(head), nums))
