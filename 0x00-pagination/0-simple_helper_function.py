#!/usr/bin/env python3
"""A function that returns a tuple of size two conataining a start
index and an end index for particular pagination parameters"""


def index_range(page: int, page_size: int):

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
