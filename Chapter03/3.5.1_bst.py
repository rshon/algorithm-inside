import collections


class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, node):
        if not self.root:
            self.root = node
            return
        
        def dfs(cur):
            if not cur:
                return node
            
            if cur.value < node.value:
                cur.right = dfs(cur.right)
            else:
                cur.left = dfs(cur.left)

            return cur
    
        dfs(self.root)
    
    def find(self, key):
        cur = self.root

        while cur:
            if cur.value == key:
                break
        
            if cur.value < key:
                cur = cur.right
            else:
                cur = cur.left
        
        return cur if cur.value == key else None

    def remove_node(self, key):
        """
                         [7]               [7]
                        /   \             /
            del ->   [4]    [9]        [3]
                    /   \             /   \
                 [3]   [5]         [1]    [2]
                /   \                        \
              [1]   [2]                       [5]
        """

        def dfs(node):
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
            elif node.value < key:
                node.right = dfs(node.right)
            elif node.value > key:
                node.left = dfs(node.left)
            
            return node
        
        return dfs(self.root)
    
    def pre_order(self, cur):
        print(cur.value, end = ' ')

        if cur.left:
            self.pre_order(cur.left)
        
        if cur.right:
            self.pre_order(cur.right)
    
    def in_order(self, cur):
        if cur.left:
            self.in_order(cur.left)
        
        print(cur.value, end = ' ')

        if cur.right:
            self.in_order(cur.right)
        
    def post_order(self, cur):
        if cur.left:
            self.post_order(cur.left)
        
        if cur.right:
            self.post_order(cur.right)
        
        print(cur.value, end = ' ')
    
    def level_order(self, cur):
        q = collections.deque([cur])

        while q:
            cur = q.popleft()
            print(cur.value, end = ' ')

            if cur.left:
                q += cur.left,

            if cur.right:
                q += cur.right,