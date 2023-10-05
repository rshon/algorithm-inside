
class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class ScheduleRegisterer:
    def __init__(self):
        self.root = None

    def search(self, start, end):
        cur = self.root

        while cur:
            if cur.start < end and start < cur.end:
                return True

            if cur.start < start:
                cur = cur.right
            else:
                cur = cur.left

        return False

    def insert(self, start, end):
        cur = self.root

        while cur:
            if cur.start < start:
                if not cur.right:
                    cur.right = TreeNode(start, end)
                    return True

                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(start, end)
                    return True

                cur = cur.left

        return False

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True

        if False == self.search(start, end):
            self.insert(start, end)
            return True

        return False


schedules = [[5, 10], [9, 15], [10, 15], [8, 12]]
sr = ScheduleRegisterer();
res = []

for start, end in schedules:
    res += sr.book(start, end),

print(res)
