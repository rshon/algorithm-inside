from typing import List
import collections


class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            return -1
        return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if not self.data:
            return 1
        return 0

    def top(self):
        if not self.data:
            return -1

        return self.data[-1]
