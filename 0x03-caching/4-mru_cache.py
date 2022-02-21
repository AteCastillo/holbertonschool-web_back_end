#!/usr/bin/python3
"""
Caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ child class inherits from basecaching, fifo"""
    def __init__(self):
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ puts key in cache """
        if key and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                pop_key = self.cache_data.popitem()
                print("DISCARD: {}".format(str(pop_key[-2])))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return (None)
        self.cache_data.move_to_end(key)
        value = self.cache_data.get(key)
        return value