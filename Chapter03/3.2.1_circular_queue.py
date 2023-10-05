from typing import List
import collections


class CircularQueue:
    def __init__(self, k: int):
        self.n = k + 1
        self.data = [0] * self.n
        self.front = 0
        self.rear = 0 

    def enqueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[self.front] = value
        self.front = (self.front + 1) % self.n
        return True 

    def dequeue(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear + 1) % self.n
        return True
        
    def front(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.rear]

    def rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.front - 1] 

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return (self.front + 1) % self.n == self.rear
