

class Bucket:
    def __init__(self, key, value):
        self.key   = key
        self.value = value


class HashMap:
    def __init__(self, size, hash_func):
        self.table_size = size
        self.table = [Bucket() for i in range(size)]
        self.hash_func = hash_func
        self.n = 0

    def insert(self, key, value):
        index = self.hash_func(key) % self.table_size
        self.table[index].insert(0, Bucket(key, value))
        self.n += 1
        return True

    def find(self, key):
        index = self.hash_func(key) % self.table_size
        for node in self.table[index]:
            if node.key == key:
                return True
    
        return False

    def remove_at(self, key):
        index = self.hash_func(key) % self.table_size
        i = 0
        found = False

        for node in self.table[index]:
            if node.key == key:
                found = True
                break
        
            i += 1
        
        if found:
            del self.table[index][i]
            return True
        
        return False


hash_map = HashMap(10, lambda x : x)
hash_map.insert(35, 'A')
hash_map.insert(37, 'C')
hash_map.insert(39, 'E')
hash_map.insert(49, 'O')    
hash_map.insert(40, 'F')
hash_map.remove(49)
print(hash_map.get(40))
hash_map.insert(59, 'Y')