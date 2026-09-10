"""
08 - User Input with Type Casting
input() always returns a string, so values must be cast to int/float
before they can be used in arithmetic.
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))

sum_int = a + b
print(sum_int)

c = float(input("Enter c: "))
d = float(input("Enter d: "))

sum_float = c + d
print(sum_float)
