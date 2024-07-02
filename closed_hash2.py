class HashTable:
    def _init_(self, size):
        self.size = size
        self.table = [None] * size
        self.hash_table=[None]*self.size

    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            i += 1
        self.table[(index + i) % self.size] = key
    
    def search(self, key):
        index = self.hash_function(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            if self.table[(index + i) % self.size] == key:
                return (index + i) % self.size
            i += 1
        return None
    
    def _str_(self):
        return str(self.table)

# Example usage:
keys = [22, 10, 47, 42, 56, 100, 50, 92, 99, 79]
hash_table = HashTable(10)

for key in keys:
    hash_table.insert(key)

print(hash_table)

# Search for some keys
for key in keys:
    print(f"Key {key} found at index: {hash_table.search(key)}")

# Output the internal state of the hash table
print("Final hash table:",hash_table)