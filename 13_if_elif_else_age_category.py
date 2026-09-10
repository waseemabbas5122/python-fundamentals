"""
13 - if / elif / else: Age Category
Chained conditions using compound logic (and).
"""

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age >= 13 and age < 18:   # 13-18
    print("Teenager")
else:
    print("Adult")
