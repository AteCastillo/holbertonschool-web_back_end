#!/usr/bin/python3
"""
Create a class LIFOCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that inherits from BaseCaching
    and is a caching system:

    You must use self.cache_data - dictionary from the parent
    class BaseCaching
    You can overload def __init__(self): but dont forget to call
    the parent init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and following
            by a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesnt exist in self.cache_data,
        return None.
    """
    def __init__(self):
        super().__init__()
    cached_list = []

    def put(self, key, item):
        """ puts key in cache """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.cached_list:
                self.cached_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                pop_key = self.cached_list.pop(-2)
                print("DISCARD: {}".format(pop_key))
                del self.cache_data[pop_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return (None)
        value = self.cache_data.get(key)
        return value
