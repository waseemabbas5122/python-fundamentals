"""
20_functions_with_parameters.py

Defining a function that takes parameters and returns a value, using
an average calculation as the example.

Agricultural relevance: this exact pattern - a function that takes a
few numbers in and returns one result - is how you'll later write
reusable helpers such as average_yield(readings) or
average_rainfall(monthly_totals) instead of repeating the same
arithmetic every time.
"""

def calculate_average(a, b, c):  # definition
    total = a + b + c
    return total / 3

print(calculate_average(2, 2, 2))
