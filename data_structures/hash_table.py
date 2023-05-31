class HashTable:
    def __init__(self):
        self.size = 50
        self.table = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.table)

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        hash_value = self._hash_function(key)
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                break


if __name__ == '__main__':
    h = HashTable()
    h.insert('apple', 5)
    print('after', h)
    h.insert('avocado', 55555)
    print('after avocado', h)
    print(h.get('avocado'))

