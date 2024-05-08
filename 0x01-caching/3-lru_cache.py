#!/usr/bin/python3
from collections import OrderedDict
"""class LRUCache that inherits from BaseCaching."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching."""

    def __init__(self):
        """Class constructor."""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = next(iter(self.order))
            self.cache_data.pop(discarded_key)
            self.order.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """Get item by key."""
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
