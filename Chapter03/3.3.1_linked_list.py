
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self, size):
        self.size = size
        self.num = 0
        self.head = Node(None)

    def insert(self, value):
        if self.num >= self.size:
            return False

        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.num += 1
        return True

    def traverse(self):
        cur = self.head.next

        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def remove(self, value):
        pre = self.head
        cur = self.head.next

        while cur:
            if cur.data == value:
                pre.next = cur.next
                self.num -= 1
                return True
            pre = cur
            cur = cur.next

        return False
    def __init__(self, size):
        self.size = size
        self.num = 0
        self.head = Node(None)


linked_list = LinkedList(3)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.traverse()
linked_list.remove(3)
linked_list.traverse()
