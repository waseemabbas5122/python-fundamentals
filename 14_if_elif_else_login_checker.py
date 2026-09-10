"""
14 - if / elif / else: Login Checker
Combining input, compound conditions (and), and branching logic
to validate a username/password pair.
"""

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("Login successful")
elif username != "admin":
    print("Username incorrect")
else:
    print("Password incorrect")
