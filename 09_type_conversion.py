"""
09 - Type Conversion
Converting between int, float, and bool, and understanding
the difference between implicit conversion and explicit casting.
"""

a = 10
b = 5
print(a / b)
print(type(a / b))   # division always returns a float

ans = int(10.0 + 3)
print(ans)
print(type(ans))

ans1 = int(10 + 5.0)   # casting the result to int
ans2 = (10 + 5.0)      # stays a float
print(ans1, type(ans1))
print(ans2, type(ans2))

val = bool(10)          # any non-zero number is True
print(val, type(val))
