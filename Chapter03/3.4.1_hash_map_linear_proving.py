from typing import List
import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums


class Node:
    def __init__(self):
        self.key   = None
        self.value = None
        self.state = 'EMPTY'    # EMPTY, FILLED, DELETED

class HashMap:
    def __init__(self, size, fp_hash):
        self.table_size = size
        self.table = [Node() for i in range(size)]
        self.n = 0
        self.fp_hash = fp_hash

    def __next(self, key):
        return 1

    def insert(self, key, value):
        index = start = self.fp_hash(key) % self.table_size
        while self.table[index].state == 'FILLED':
            index = (index + self.__next(key)) % self.table_size
            if index == start:  # table is full
                return False

        self.table[index].state = 'FILLED'
        self.table[index].key   = key
        self.table[index].value = value
        self.n += 1
        return True

    def find(self, key):
        index = start = self.fp_hash(key) % self.table_size
        while self.table[index] != 'EMPTY':
            if self.table[index].state == 'FILLED' and self.table[index].key == key:
                return index
            index = (index + self.__next(key)) % self.table_size
            if index == start:
                return -1
        return -1

    def get(self, key):
        index = self.find(key)
        if -1 == index:
            return -1
        return self.table[index].value

    def remove(self, key):
        index = self.find(key)
        if -1 == index:
            return False
        self.remove_at(index)
        return True

    def remove_at(self, pos):
        if pos < 0 or pos >= self.table_size or self.n == 0:
            return False
        if self.table[pos].state != 'FILLED':
            return False
        self.table[pos].state = 'DELETED'
        self.n -= 1
        return True

    def print_all(self):
        i = 0
        for node in self.table:
            print('{:04} : '.format(i), node.key, node.value, node.state)
            i += 1
        print()


hash_map = HashMap(10, lambda x : x)
hash_map.insert(35, 'A')
hash_map.insert(37, 'C')
hash_map.insert(39, 'E')
hash_map.insert(49, 'O')    
hash_map.insert(40, 'F')
hash_map.remove(49)
print(hash_map.get(40))
hash_map.insert(59, 'Y')
