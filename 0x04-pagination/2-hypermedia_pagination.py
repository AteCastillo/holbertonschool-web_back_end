#!/usr/bin/env python3
"""
Task 1, python simple pagination func
"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return a dictionry containing key-val pairs:
            page_size:the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        hyper_dict = {}
        all_data = self.dataset()
        data_size = len(all_data)
        ranger = (page * page_size)
        total_page = (data_size + 1) / page_size
        if ranger > data_size:
            hyper_dict['page_size'] = 0
            hyper_dict['page'] = page
            hyper_dict['data'] = []
            hyper_dict['next_page'] = None
            hyper_dict['prev_page'] = (page - 1)
            hyper_dict['total_pages'] = (total_page + 1)

        else:
            hyper_dict['page_size'] = page_size
            hyper_dict['page'] = page
            hyper_dict['data'] = self.get_page(page, page_size)
            hyper_dict['next_page'] = (page + 1)
            if hyper_dict['page'] == 1:
                hyper_dict['prev_page'] = None
            else:
                hyper_dict['prev_page'] = (page - 1)
            hyper_dict['total_pages'] = total_page
        return hyper_dict
gitpu