"""
17_while_loop_basics.py

Core while-loop pattern: repeat an action while a condition stays true,
using a manually controlled counter (iterator).

Agricultural relevance: while-loops fit situations where you don't know
in advance how many repetitions are needed - e.g. "keep checking soil
moisture until it reaches field capacity."
"""

i = 1
while i <= 15:
    print("hello world", i)
    i += 1

print("after loop, i =", i)
