"""
15_for_loop_basics.py

Core for-loop patterns: looping over a range of numbers, looping over
each character in a string, and checking membership with 'in'.

Agricultural relevance: this is the same pattern used later to loop
through a list of fields, farmers, or sample IDs and check a condition
for each one (e.g. "does this field's ID contain a given zone code?").
"""

# Loop through a sequence of numbers (1 to 17)
for x in range(17):
    print(x + 1)

print("---")

# Loop through each character in a string
name = "waseem"
for var in name:
    print(var)

# Membership check using 'in'
if "e" in name:
    print("exist")
