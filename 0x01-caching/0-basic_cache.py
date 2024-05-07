#!/usr/bin/python3
"""BasicCache that inherits from BaseCaching and is a caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching."""

    def put(self, key, item):
        """Add an item to the cach."""

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
