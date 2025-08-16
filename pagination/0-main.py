#!/usr/bin/env python3
index_range = __import__('0-simple_helper_function').index_range

print(type(index_range(1, 7)))
print(index_range(1, 7))
print(type(index_range(page=3, page_size=15)))
print(index_range(page=3, page_size=15))
