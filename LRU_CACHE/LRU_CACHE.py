import collections

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        # Move the key to the front of the cache
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        # If the key already exists, update its value
        if key in self.cache:
            self.cache[key] = value
            return

        # If the cache is full, evict the least recently used key
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        # Add the new key to the cache
        self.cache[key] = value

    def __len__(self):
        return len(self.cache)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    assert cache.get(1) == 1

    cache.put(2, 2)
    assert cache.get(2) == 2

    cache.put(3, 3)  # evicts key 1
    assert cache.get(1) == -1

    cache.put(2, 4)
    assert cache.get(2) == 4

    cache.put(4, 4)  # evicts key 3
    assert cache.get(3) == -1

    assert cache.get(5) == -1
