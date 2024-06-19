#!/usr/bin/python3
try:
    number=98
    print(f"{number} Battery street")
except NameError:
    print("Variable 'number' is not defined.")
except Exception as e:
    print(f"An error occurred: {e}")
