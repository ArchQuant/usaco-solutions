import sys
sys.stdin = open("input", "r")

exist = [False] * 200
# IM - for "find"-type task for a fixed pool, 
# use exist-flag with vector, not set (hash less efficient)
for c in input():
    exist[ord(c)] = True
for i in range(26):
    letter = ord('a') + i
    if not exist[letter]:
        print(chr(letter))
        break

# OR use counter:
from collections import defaultdict
count = defaultdict(int)

for c in input():
    count[c] += 1
for i in range(26):
    letter = chr(ord('a') + i)
    if count[letter] == 0:
        print(letter)
        break