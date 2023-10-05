
class Node:
    def __init__(self, value):
        self.value = value


class HeapQueue:
    def __init__(self):
        self.num = 0        # except root (no note)
        self.nodes = []

    def __deinit__(self):
        pass

    def insert(self, value):
        self.nodes.append(Node(value))
        self.num += 1
        self.upheap()

    def __swap(self, lnode, rnode):
        lnode.value, rnode.value = rnode.value, lnode.value

    def upheap(self):
        cur_idx = self.num - 1
        cur = self.nodes[cur_idx]

        while cur_idx > 0:
            par_idx = (cur_idx - 1) // 2
            par = self.nodes[par_idx]
            if cur.value <= par.value:
                break

            self.__swap(par, cur)
            cur = self.nodes[par_idx]
            cur_idx = par_idx

    def downheap(self, cur_idx):
        cur = self.nodes[cur_idx]

        while cur_idx < self.num // 2:
            chd_idx = 1 if cur_idx == 0 else ((cur_idx + 1) * 2 - 1)
            if chd_idx + 1 < self.num and \
                    self.nodes[chd_idx].value < self.nodes[chd_idx + 1].value:
                chd_idx += 1

            if cur.value < self.nodes[chd_idx].value:
                self.__swap(cur, self.nodes[chd_idx])

            cur = self.nodes[chd_idx]
            cur_idx = chd_idx

    def extract(self):
        if 0 == self.num:
            return None

        node = self.nodes[0]
        self.nodes[0] = self.nodes[self.num - 1]
        del self.nodes[self.num - 1]
        self.num -= 1

        if self.num > 0:
            self.downheap(0)

        return node.value

    def empty(self):
        return True if self.num == 0 else False


def unit_test():
    heapq = HeapQueue()
    heapq.insert(5)
    heapq.insert(3)
    heapq.insert(7)
    heapq.insert(4)
    heapq.insert(10)
    print(heapq.extract())
    print(heapq.extract())
    print(heapq.extract())
    print(heapq.extract())
    print(heapq.extract())
    print(heapq.extract())


unit_test()