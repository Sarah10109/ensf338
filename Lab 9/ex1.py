import hashlib

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.left_table = {i: [] for i in range(buckets)}
        self.right_table = {i: [] for i in range(buckets)}

    def _hash(self, key, table):
        if table == 'left':
            hash_object = hashlib.sha1(bytes(key, 'utf-8'))
        else:  # right table
            hash_object = hashlib.md5(bytes(key, 'utf-8'))
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16) % self.buckets

    def insert(self, key, value):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))
    
    # Q2
    def insert(self, key, value):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))
            
    # Q3
    def lookup(self, key):
        left_hash = self._hash(key, 'left')
        right_hash = self._hash(key, 'right')

        for k, v in self.left_table[left_hash]:
            if k == key:
                return v

        for k, v in self.right_table[right_hash]:
            if k == key:
                return v

        return None  # key not found