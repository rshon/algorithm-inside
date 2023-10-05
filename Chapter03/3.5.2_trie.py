from typing import List
import collections


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.child = {}
        self.eow = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = TrieNode(ch)
            
            cur = cur.child[ch]
        
        cur.eow = True
    
    def get_starts_with(self, prefix: str) -> List:
        cur = self.root

        for ch in prefix:
            if ch not in cur.child:
                return None
            
            cur = cur.child[ch]
        
        if not cur:
            return None
    
        q = collections.deque([cur, prefix])
        res = []

        while q:
            cur, word = q.popleft()
            if cur.eow:
                res += word,

            for node in cur.child.values():
                q.append((node, word + node.letter))
        
        return res

    def starts_with(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.child:
                return False
        
            cur = cur.child[ch]
        
        return True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.child:
                return False
        
            cur = cur.child[ch]

        return cur.eow


trie = Trie()
trie.insert("bst")
trie.insert("best")
trie.insert("bestow")
trie.insert("black")
trie.insert("blank")
print('starts with b')
print(trie.get_starts_with("b"))


