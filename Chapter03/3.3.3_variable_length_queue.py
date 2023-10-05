from typing import List
import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = next


class DoubleLinkedList:
    def __init__(self, size):
        self.size = size
        self.num = 0        
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert(self, value):
        if self.num >= self.size:
            return False

        node = Node(value)

        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
        self.num += 1
        return True

    def traverse(self):
        cur = self.head.next

        while cur != self.tail:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value):
        cur = self.head.next

        while cur != self.tail:
            if cur.data == value:
                cur.next.pre = cur.pre
                cur.pre.next = cur.next
                self.num -= 1
                return True
            cur = cur.next

        return False

    def remove_at_last(self):
        if self.num == 0:
            return None
        node = self.tail.pre
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre
        self.num -= 1
        return node


class Queue:
    def __init__(self, n):
        self.dll = DoubleLinkedList(n)

    def enqueue(self, value) -> bool:
        return self.dll.insert(value)

    def dequeue(self) -> Node:
        return self.dll.removeAtLast()

