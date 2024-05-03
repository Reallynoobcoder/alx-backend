#!/usr/bin/env python3
"""The function should return a tuple of size two."""


def index_range(page, page_size):
    """Retuen range of index."""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    index = (start_index, end_index)

    return index
