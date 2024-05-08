#!/usr/bin/python3
"""class MRUCache that inherits from BaseCaching."""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching."""

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
            mru_key = next(reversed(self.order))
            self.cache_data.pop(mru_key)
            self.order.popitem()
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """Get item by key."""
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
