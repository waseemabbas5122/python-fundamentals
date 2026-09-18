"""
16_for_loop_range_step.py

Using range(start, stop, step) to control exactly which values a loop
produces, instead of stepping through every number by default.

Agricultural relevance: step-based ranges are useful for things like
sampling every nth plant in a row, or checking sensor readings every
few hours instead of every minute.
"""

# range(start, stop, step)
for x in range(1, 8, 2):
    print(x)
