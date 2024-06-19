#!/usr/bin/python3
number = 98  

try:
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    print(f"{number} Battery street")
except TypeError as e:
    print(e)
