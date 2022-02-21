#!/usr/bin/env python3
"""
Return tuple of of size two
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    takes two integer arguments page with default value 1
    and page_size with default value 10.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginate the dataset, return the appropriate page of the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        all_data = self.dataset()
        page_list = []

        ''' check if the number of entries is lrgr than entire dataset'''
        ranger = (page * page_size)
        if ranger > len(all_data):
            '''retrn empty lst if lrgr thn all data'''
            return page_list

        '''betwn index-strt and index-end cre8 new-pg and append to pg-lst'''
        indexes = index_range(page, page_size)
        for i in range(indexes[0], indexes[1]):
            new_page = all_data[i]
            page_list.append(new_page)
        return page_list
