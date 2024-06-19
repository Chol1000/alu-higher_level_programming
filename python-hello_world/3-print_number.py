#!/usr/bin/python3

number = 98  # Example integer value

try:
    # Printing the integer followed by "Battery street"
    print(f"{number} Battery street")
except TypeError:
    print("number must be an integer")
