#!/usr/bin/python3
"""Basic Lifo caching."""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching."""

    def __init__(self):
        """Class constructor."""

        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add item to the cach."""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order[-2]
            print("DISCARD: {}".format(discarded_key))
            del self.cache_data[discarded_key]

    def get(self, key):
        """Get item by key."""

        if key is None or key is not self.cache_data:
            return None

        return self.cache_data[key]
