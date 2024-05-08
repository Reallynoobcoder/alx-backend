#!/usr/bin/python3
"""class LRUCache that inherits from BaseCaching."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching."""

    def __init__(self):
        """Class constructor."""

        super().__init__()

    def put(self, key, item):
        """Add item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
