"""
10 - if / elif / else: Traffic Light
Basic branching logic using multiple elif conditions.
"""

color = input("Enter color: ")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("wrong traffic color")
