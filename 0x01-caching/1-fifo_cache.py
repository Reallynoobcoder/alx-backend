#!/usr/bin/python3
"""Basic FIFO caching."""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching."""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add item to the cach."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(discarded_key))
            del self.cache_data[discarded_key]

    def get(self, key):
        """Get item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
