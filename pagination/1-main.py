#!/usr/bin/env python3
Server = __import__('1-simple_pagination').Server

server = Server()

try:
    server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    server.get_page(2, 'Bob')  # type: ignore
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
