
class RadixNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RadixTree:
    def __init__(self, m):
        self.root = None
        self.m = m
        self.fmt = '{:0' + str(self.m) + 'b}'

    def __deinit__(self):
        ...

    def convert_bits(self, key):
        assert(len('{:b}'.format(key)) <= self.m)
        return self.fmt.format(key)

    def find(self, key):
        cur = self.root
        bits = self.convert_bits(key)

        while cur and i >= 0:
            if cur.value == key:
                break

            if '0' == bits[i]:
                cur = cur.left
            else:
                cur = cur.right

            i -= 1

        return cur if cur.value == key else None

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        def dfs(cur, bits, i):
            if not cur:
                return node

            if '0' == bits[i]:
                cur.left = dfs(cur.left, bits, i - 1)
            else:
                cur.right = dfs(cur.right, bits, i - 1)

            return cur

        bits = self.convert_bits(node.value)
        dfs(self.root, bits, len(bits) - 1)

    def remove_node(self, key):
        def dfs(node, bits, i):
            if not node:
                return None

            if node.value == key:
                if not node.left and not node.right:
                    return None

                if not node.left or not node.right:
                    return node.left or node.right

                cur = node.left
                while cur.right:
                    cur = cur.right
                cur.right = node.right
                return node.left
            elif '1' == bits[i]:
                node.right = dfs(node.right, bits, i - 1)
            elif '0' == bits[i]:
                node.left = dfs(node.left, bits, i - 1)
            return node

        bits = self.convert_bits(key)
        return dfs(self.root, bits, len(bits) - 1)

    def pre_order(self, cur, print_func=print):
        print_func(cur.value, end=' ')

        if cur.left != None:
            self.pre_order(cur.left, print_func)

        if cur.right != None:
            self.pre_order(cur.right, print_func)

    def in_order(self, cur, print_func=print):
        if cur.left != None:
            self.in_order(cur.left, print_func)

        print_func(cur.value, end=' ')

        if cur.right != None:
            self.in_order(cur.right, print_func)

    def post_order(self, cur, print_func=print):
        if cur.left != None:
            self.post_order(cur.left, print_func)

        if cur.right != None:
            self.post_order(cur.right, print_func)

        print_func(cur.value, end=' ')

    def level_order(self, cur, print_func=print):
        q = [cur]

        while q:
            cur = q.pop(0)
            print_func(cur.value, end=' ')

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    def traverse(self, type, print_func=print):
        if type == 'pre':
            self.pre_order(self.root, print_func)
        elif type == 'in':
            self.in_order(self.root, print_func)
        elif type == 'post':
            self.post_order(self.root, print_func)
        elif type == 'level':
            self.level_order(self.root, print_func)
        print()


tree = RadixTree(8)

values = ['a', 'b', 'e', 't', 'k', 'w', 'p', 'v']
for val in values:
    tree.insert(RadixNode(ord(val)))

def print_value(val, end):
    print(chr(val), end, end='')

print('pre order')
tree.traverse('pre', print_value)

print('\nin order')
tree.traverse('in', print_value)

print('\npost order')
tree.traverse('post', print_value)

print('\nlevel order')
tree.traverse('level', print_value)

print('removing 5')
tree.remove_node(5)

tree.traverse('post', print_value)
tree.traverse('level', print_value)